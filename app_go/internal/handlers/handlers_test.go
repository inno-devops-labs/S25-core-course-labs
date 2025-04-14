// Package handlers_test contains tests for numerologist API handlers.
package handlers_test

import (
	"net/http"
	"net/http/httptest"
	"os"
	"testing"

	"github.com/m0t9/S25-core-course-labs/app_go/internal/server"
)

// TestRootHandler tests whether API server returns 200th status code.
func TestRootHandler(t *testing.T) {
	t.Parallel()

	// To properly import static content.
	os.Chdir("../../cmd/numerologist")

	app := server.New()

	// Building a request to root page.
	req := httptest.NewRequest("GET", "/", nil)
	resp, err := app.Test(req)
	if err != nil {
		t.Fatalf("request to API failed with following error: %s", err)
	}

	if resp.StatusCode != http.StatusOK {
		t.Fatalf("response to API returned status code %d, that differs from 200",
			resp.StatusCode)
	}
}
