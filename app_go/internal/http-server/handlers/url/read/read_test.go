package read_test

import (
	"context"
	"encoding/json"
	"errors"
	"net/http"
	"net/http/httptest"
	"testing"

	"url-shortener/internal/http-server/handlers/url/read"
	"url-shortener/internal/http-server/handlers/url/read/mocks"
	"url-shortener/internal/lib/logger/handlers/slogdiscard"
	"url-shortener/internal/storage"

	"github.com/go-chi/chi/v5"
	"github.com/stretchr/testify/require"
)

func TestReadHandler(t *testing.T) {
	// Test cases for the read handler:
	// - "Success": When a valid alias is provided and the URL is found,
	//    expect a redirect (HTTP 302 Found) with Location header set.
	// - "Empty Alias": When the alias is empty,
	//    expect a 422 Unprocessable Entity with a JSON error response.
	// - "URL Not Found": When the URLReader returns storage.ErrURLNotFound,
	//    expect a 404 Not Found with a JSON error response.
	// - "Internal Error": When the URLReader returns an unexpected error,
	//    expect a 500 Internal Server Error with a JSON error response.
	cases := []struct {
		name          string
		alias         string
		returnedURL   string
		mockError     error
		expectedCode  int
		expectedError string // substring that must appear in error message; empty means success
	}{
		{
			name:         "Success",
			alias:        "test_alias",
			returnedURL:  "https://example.com",
			expectedCode: http.StatusFound, // 302 redirect
		},
		{
			name:          "Empty Alias",
			alias:         "",
			expectedCode:  http.StatusUnprocessableEntity,
			expectedError: "incorrect alias",
		},
		{
			name:          "URL Not Found",
			alias:         "not_found_alias",
			mockError:     storage.ErrURLNotFound,
			expectedCode:  http.StatusNotFound,
			expectedError: "no URl with such alias",
		},
		{
			name:          "Internal Error",
			alias:         "test_alias",
			mockError:     errors.New("unexpected error"),
			expectedCode:  http.StatusInternalServerError,
			expectedError: "failed to find url",
		},
	}

	for _, tc := range cases {
		tc := tc // capture range variable
		t.Run(tc.name, func(t *testing.T) {
			// Create a mock URLReader.
			urlReaderMock := mocks.NewURLReader(t)

			// When the alias is non-empty and we expect the handler to call GetURL,
			// set up the expectation on the mock.
			if tc.alias != "" {
				urlReaderMock.
					On("GetURL", tc.alias).
					Return(tc.returnedURL, tc.mockError).
					Once()
			}

			// Create the handler.
			handler := read.New(slogdiscard.NewDiscardLogger(), urlReaderMock)

			// Build a new HTTP request. The method doesn't matter much here,
			// so we can use GET.
			req, err := http.NewRequest(http.MethodGet, "/"+tc.alias, nil)
			require.NoError(t, err)

			// Create a chi route context and inject the alias as URL parameter.
			rctx := chi.NewRouteContext()
			rctx.URLParams.Add("alias", tc.alias)
			// Embed the route context into the request context.
			req = req.WithContext(context.WithValue(req.Context(), chi.RouteCtxKey, rctx))

			// Use httptest.ResponseRecorder to capture the response.
			rr := httptest.NewRecorder()

			// Call the handler.
			handler.ServeHTTP(rr, req)

			// Assert on the HTTP status code.
			require.Equal(t, tc.expectedCode, rr.Code)

			// On success, we expect a redirect to the returned URL.
			if tc.expectedCode == http.StatusFound {
				// StatusFound (302) response should contain a Location header.
				loc := rr.Header().Get("Location")
				require.Equal(t, tc.returnedURL, loc)
			} else {
				// For error cases, the handler returns a JSON response.
				// Unmarshal the JSON error response.
				var resp map[string]interface{}
				err := json.Unmarshal(rr.Body.Bytes(), &resp)
				require.NoError(t, err)
				errMsg, ok := resp["error"].(string)
				require.True(t, ok, "expected error message in response")
				require.Contains(t, errMsg, tc.expectedError)
			}
		})
	}
}
