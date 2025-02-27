package delete_test

import (
	"encoding/json"
	"errors"
	"net/http"
	"net/http/httptest"
	"net/url"
	"testing"

	"url-shortener/internal/http-server/handlers/url/delete"
	"url-shortener/internal/http-server/handlers/url/delete/mocks"
	"url-shortener/internal/lib/logger/handlers/slogdiscard"
	"url-shortener/internal/storage"

	"github.com/stretchr/testify/require"
)

func TestDeleteHandler(t *testing.T) {
	// Define test cases.
	// - "Success": When a valid alias is provided and deletion succeeds.
	// - "Empty Alias": When no alias is provided in the query string.
	// - "URL Not Found": When DeleteURL returns storage.ErrURLNotFound.
	// - "Internal Error": When DeleteURL returns an unexpected error.
	cases := []struct {
		name          string
		alias         string
		mockError     error
		expectedCode  int
		expectedError string // substring that must appear in error message; empty means success
	}{
		{
			name:         "Success",
			alias:        "test_alias",
			expectedCode: http.StatusOK,
		},
		{
			name:          "Empty Alias",
			alias:         "",
			expectedCode:  http.StatusUnprocessableEntity,
			expectedError: "incorrect alias",
		},
		{
			name:          "URL Not Found",
			alias:         "not_found",
			mockError:     storage.ErrURLNotFound,
			expectedCode:  http.StatusNotFound,
			expectedError: "no URl with such alias",
		},
		{
			name:          "Internal Error",
			alias:         "test_alias",
			mockError:     errors.New("unexpected error"),
			expectedCode:  http.StatusInternalServerError,
			expectedError: "failed to add url",
		},
	}

	for _, tc := range cases {
		tc := tc // capture range variable
		t.Run(tc.name, func(t *testing.T) {
			// Create a new mock for URLDeleter.
			urlDeleterMock := mocks.NewURLDeleter(t)

			// For non-empty alias, the handler is expected to call DeleteURL.
			if tc.alias != "" {
				urlDeleterMock.
					On("DeleteURL", tc.alias).
					Return(tc.mockError).
					Once()
			}

			// Create the handler.
			handler := delete.New(slogdiscard.NewDiscardLogger(), urlDeleterMock)

			// Build the request URL with the alias query parameter.
			reqURL := "/delete"
			if tc.alias != "" {
				// Append the alias as a query parameter.
				reqURL += "?alias=" + url.QueryEscape(tc.alias)
			}
			req, err := http.NewRequest(http.MethodDelete, reqURL, nil)
			require.NoError(t, err)

			rr := httptest.NewRecorder()
			handler.ServeHTTP(rr, req)

			// Verify the HTTP status code.
			require.Equal(t, tc.expectedCode, rr.Code)

			// On success, the handler writes only the status code (with an empty body).
			if tc.expectedCode == http.StatusOK {
				require.Empty(t, rr.Body.Bytes())
			} else {
				// For error cases, expect a JSON error response.
				require.Contains(t, rr.Header().Get("Content-Type"), "application/json")

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
