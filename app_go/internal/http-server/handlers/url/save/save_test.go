package save_test

import (
	"encoding/json"
	"errors"
	"net/http"
	"net/http/httptest"
	"net/url"
	"strings"
	"testing"

	"github.com/stretchr/testify/mock"
	"github.com/stretchr/testify/require"

	"url-shortener/internal/http-server/handlers/url/save"
	"url-shortener/internal/http-server/handlers/url/save/mocks"
	"url-shortener/internal/lib/logger/handlers/slogdiscard"
	"url-shortener/internal/storage"
)

func TestSaveHandler(t *testing.T) {
	// Each test case defines:
	// - name: name of the test case.
	// - alias: form value for alias (empty string is allowed).
	// - url: form value for url.
	// - respError: expected error substring in the JSON response, if any.
	// - mockError: error to be returned by the URLSaver mock.
	//
	// Note that on success the handler returns HTML (rendered list item),
	// and on error it returns a JSON response with an "error" field.
	cases := []struct {
		name      string
		alias     string
		url       string
		respError string
		mockError error
	}{
		{
			name:  "Success",
			alias: "test_alias",
			url:   "https://google.com",
		},
		{
			name:  "Empty alias",
			alias: "",
			url:   "https://google.com",
		},
		{
			name:      "Empty URL",
			url:       "",
			alias:     "some_alias",
			respError: "field URL is a required field",
		},
		{
			name:      "Invalid URL",
			url:       "some invalid URL",
			alias:     "some_alias",
			respError: "field URL is not a valid URL",
		},
		{
			name:      "SaveURL Error",
			alias:     "test_alias",
			url:       "https://google.com",
			respError: "failed to add url",
			mockError: errors.New("unexpected error"),
		},
		{
			name:      "URL Already Exists",
			alias:     "test_alias",
			url:       "https://google.com",
			respError: "url already exists",
			mockError: storage.ErrURLExists,
		},
	}

	for _, tc := range cases {
		tc := tc // capture range variable
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()

			// Create a mock URLSaver.
			urlSaverMock := mocks.NewURLSaver(t)

			// For cases that are expected to go to the SaveURL call (i.e. no validation errors)
			// we set the expectation. Note that when validation fails (Empty URL/Invalid URL)
			// the handler returns before calling SaveURL.
			if tc.respError == "" || tc.mockError != nil {
				// When alias is empty, the handler generates a random alias.
				// We can’t predict it, so use a matcher that just requires a non-empty string.
				var aliasMatcher interface{}
				if tc.alias == "" {
					aliasMatcher = mock.MatchedBy(func(s string) bool {
						return s != ""
					})
				} else {
					aliasMatcher = tc.alias
				}
				urlSaverMock.On("SaveURL", tc.url, aliasMatcher).
					Return(int64(1), tc.mockError).
					Once()
			}

			// Create the handler.
			h := save.New(slogdiscard.NewDiscardLogger(), urlSaverMock)

			// Build form-encoded request body.
			form := url.Values{}
			form.Set("url", tc.url)
			form.Set("alias", tc.alias)
			reqBody := strings.NewReader(form.Encode())

			req, err := http.NewRequest(http.MethodPost, "/save", reqBody)
			require.NoError(t, err)
			// Set proper header so that the body is parsed as form data.
			req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

			rr := httptest.NewRecorder()
			h.ServeHTTP(rr, req)

			// Determine expected HTTP status code.
			var expectedStatus int
			// When validation fails, the handler returns 422.
			// When the SaveURL returns storage.ErrURLExists, it returns 409.
			// When SaveURL returns any other error, it returns 500.
			// Otherwise (success) it returns 200.
			if tc.respError != "" {
				if errors.Is(tc.mockError, storage.ErrURLExists) {
					expectedStatus = http.StatusConflict
				} else if tc.mockError != nil {
					expectedStatus = http.StatusInternalServerError
				} else {
					expectedStatus = http.StatusUnprocessableEntity
				}
			} else {
				expectedStatus = http.StatusOK
			}
			require.Equal(t, expectedStatus, rr.Code)

			// Based on status code, assert response content.
			if expectedStatus == http.StatusOK {
				// On success, the handler returns an HTML fragment.
				require.Contains(t, rr.Header().Get("Content-Type"), "text/html")
				body := rr.Body.String()
				// The template renders a <li> element with an id that includes the alias.
				// When the alias was provided we expect that alias; when it was empty,
				// a random non-empty alias is generated.
				if tc.alias != "" {
					require.Contains(t, body, `<li id="url-`+tc.alias+`">`)
					require.Contains(t, body, "/urls/"+tc.alias)
				} else {
					// For a random alias, simply check that some id is rendered.
					require.Contains(t, body, `<li id="url-`)
					require.Contains(t, body, "/urls/")
				}
			} else {
				// On error, the handler returns a JSON error response.
				require.Contains(t, rr.Header().Get("Content-Type"), "application/json")
				var respData map[string]interface{}
				require.NoError(t, json.Unmarshal(rr.Body.Bytes(), &respData))
				// Check that the error message appears in the response.
				errMsg, ok := respData["error"].(string)
				require.True(t, ok, "expected error message in response")
				require.Contains(t, errMsg, tc.respError)
			}
		})
	}
}
