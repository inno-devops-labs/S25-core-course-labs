package manage

import (
	"html/template"
	"log/slog"
	"net/http"
)

type URLLister interface {
	GetAllURLs() ([]string, error)
}

type URLData struct {
	Alias string
	Path  string
}

func New(log *slog.Logger, urlLister URLLister, tmpl *template.Template) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		const op = "handlers.manage.New"

		log = log.With(slog.String("op", op))

		urls, err := urlLister.GetAllURLs()
		if err != nil {
			log.Error("failed to fetch URLs", slog.String("error", err.Error()))
			http.Error(w, "failed to load page", http.StatusInternalServerError)
			return
		}

		data := make([]URLData, len(urls))
		for i, val := range urls {
			data[i] = URLData{
				Alias: val,
				Path:  "/urls/" + val,
			}
		}

		err = tmpl.Execute(w, struct {
			URLs []URLData
		}{
			URLs: data,
		})
		if err != nil {
			log.Error("failed to render template", slog.String("error", err.Error()))
		}
	}
}
