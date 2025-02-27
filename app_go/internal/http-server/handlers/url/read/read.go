package read

import (
	"errors"
	"log/slog"
	"net/http"
	"url-shortener/internal/lib/api/response"
	"url-shortener/internal/lib/logger/sl"
	"url-shortener/internal/storage"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/go-chi/render"
)

type Request struct {
	Alias string
}

type Response struct {
	response.Response
	Url string `json:"url"`
}

const (
	alias = "alias"
)

type URLReader interface {
	GetURL(alias string) (string, error)
}

func New(log *slog.Logger, urlReader URLReader) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		const op = "handlers.url.read.New"

		log = log.With(
			slog.String("op", op),
			slog.String("request_id", middleware.GetReqID(r.Context())),
		)

		var req Request

		req.Alias = chi.URLParam(r, alias)
		if len(req.Alias) <= 0 {
			log.Error(
				"incorrect alias url parameter",
				slog.String("alias", req.Alias),
			)
			render.Status(r, http.StatusUnprocessableEntity)
			render.JSON(w, r, response.Error("incorrect alias"))
			return
		}

		url, err := urlReader.GetURL(req.Alias)
		if errors.Is(err, storage.ErrURLNotFound) {
			log.Error("no URL with such alias", slog.String("alias", req.Alias))

			render.Status(r, http.StatusNotFound)
			render.JSON(w, r, response.Error("no URl with such alias"))

			return
		}
		if err != nil {
			log.Error("failed to find url", sl.Err(err))

			render.Status(r, http.StatusInternalServerError)
			render.JSON(w, r, response.Error("failed to find url"))

			return
		}

		log.Info("url found", slog.String("alias", req.Alias))

		http.Redirect(w, r, url, http.StatusFound)
	}
}

func responseOK(w http.ResponseWriter, r *http.Request, url string) {
	render.JSON(w, r, Response{
		Response: response.OK(),
		Url:      url,
	})
}
