package sqlite_test

import (
	"strings"
	"testing"

	"url-shortener/internal/storage"
	"url-shortener/internal/storage/sqlite"
)

// newTestStorage creates a new Storage instance using an in‑memory database.
func newTestStorage(t *testing.T) *sqlite.Storage {
	t.Helper()
	s, err := sqlite.New(":memory:")
	if err != nil {
		t.Fatalf("failed to create sqlite storage: %v", err)
	}
	return s
}

func TestSaveAndGetURL(t *testing.T) {
	store := newTestStorage(t)

	// Save a URL.
	urlToSave := "https://example.com"
	alias := "exmpl"
	id, err := store.SaveURL(urlToSave, alias)
	if err != nil {
		t.Fatalf("SaveURL failed: %v", err)
	}
	if id <= 0 {
		t.Errorf("expected a positive id, got %d", id)
	}

	// Retrieve the URL.
	gotURL, err := store.GetURL(alias)
	if err != nil {
		t.Fatalf("GetURL failed: %v", err)
	}
	if gotURL != urlToSave {
		t.Errorf("expected URL %q, got %q", urlToSave, gotURL)
	}
}

func TestSaveURL_DuplicateAlias(t *testing.T) {
	store := newTestStorage(t)

	urlToSave := "https://example.com"
	alias := "dup"

	// Save the first URL.
	_, err := store.SaveURL(urlToSave, alias)
	if err != nil {
		t.Fatalf("first SaveURL failed: %v", err)
	}

	// Attempt to save another URL with the same alias.
	_, err = store.SaveURL("https://another.com", alias)
	if err == nil {
		t.Fatal("expected error for duplicate alias, got nil")
	}

	// Check that the error message indicates a duplicate alias.
	if !strings.Contains(err.Error(), storage.ErrURLExists.Error()) {
		t.Errorf("expected error to contain %q, got %s", storage.ErrURLExists, err.Error())
	}
}

func TestGetURL_NotFound(t *testing.T) {
	store := newTestStorage(t)

	// Attempt to get a URL for a non-existent alias.
	_, err := store.GetURL("nonexistent")
	if err == nil {
		t.Fatal("expected error for non-existing alias, got nil")
	}
	if err != storage.ErrURLNotFound {
		t.Errorf("expected storage.ErrURLNotFound, got %v", err)
	}
}

func TestGetAllURLs(t *testing.T) {
	store := newTestStorage(t)

	// Insert several entries.
	entries := []struct {
		url   string
		alias string
	}{
		{"https://example.com", "ex1"},
		{"https://google.com", "ex2"},
	}
	for _, entry := range entries {
		_, err := store.SaveURL(entry.url, entry.alias)
		if err != nil {
			t.Fatalf("SaveURL failed for alias %q: %v", entry.alias, err)
		}
	}

	// Retrieve all aliases.
	aliases, err := store.GetAllURLs()
	if err != nil {
		t.Fatalf("GetAllURLs failed: %v", err)
	}
	if len(aliases) != len(entries) {
		t.Errorf("expected %d aliases, got %d", len(entries), len(aliases))
	}
	// Check that all expected aliases are present.
	for _, entry := range entries {
		found := false
		for _, a := range aliases {
			if a == entry.alias {
				found = true
				break
			}
		}
		if !found {
			t.Errorf("alias %q not found in %v", entry.alias, aliases)
		}
	}
}

func TestDeleteURL(t *testing.T) {
	store := newTestStorage(t)

	urlToSave := "https://example.com"
	alias := "del"

	// Save a URL.
	_, err := store.SaveURL(urlToSave, alias)
	if err != nil {
		t.Fatalf("SaveURL failed: %v", err)
	}

	// Delete the URL.
	err = store.DeleteURL(alias)
	if err != nil {
		t.Fatalf("DeleteURL failed: %v", err)
	}

	// Attempt to get the URL after deletion.
	_, err = store.GetURL(alias)
	if err == nil {
		t.Fatal("expected error when retrieving deleted alias, got nil")
	}
	if err != storage.ErrURLNotFound {
		t.Errorf("expected storage.ErrURLNotFound, got %v", err)
	}

	// Attempt to delete an alias that does not exist.
	err = store.DeleteURL("nonexistent")
	if err == nil {
		t.Fatal("expected error when deleting non-existing alias, got nil")
	}
	if !strings.Contains(err.Error(), storage.ErrURLNotFound.Error()) {
		t.Errorf("expected error to contain %q, got %v", storage.ErrURLNotFound, err)
	}
}
