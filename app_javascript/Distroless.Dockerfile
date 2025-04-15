# Use a non-root base image for the build stage
FROM gcr.io/distroless/nodejs20-debian12:nonroot AS build-env
WORKDIR /app
COPY ./src ./
FROM pierrezemb/gostatic
COPY --from=build-env /app /srv/http
EXPOSE 8080
CMD ["-port", "8080"]
