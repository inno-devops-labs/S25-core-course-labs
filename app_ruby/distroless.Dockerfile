FROM ruby:3.4.1-slim AS builder

ENV BUNDLE_WITHOUT=development:test \
    LANG=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc=4:12.2.0-3 \
        musl-dev=1.2.3-1 \
        tzdata=2024b-0+deb12u1 \
        make=4.3-4.1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN gem install nio4r:2.7.4 -- --use-system-libraries && \
    gem install bundler:2.6.3

COPY Gemfile Gemfile.lock ./

RUN bundle install && cp "$(which ruby)" /app

COPY public/styles.css views/index.erb app.rb config.ru ./

FROM gcr.io/distroless/base-debian12:nonroot AS runtime

WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local /usr/local
COPY --from=builder /usr/lib /usr/lib
COPY --from=builder /usr/local/bin/ruby /usr/local/bin/ruby
COPY --from=builder /usr/local/lib/ruby/3.4.0 /usr/local/lib/ruby/3.4.0
COPY --from=builder /usr/local/bundle /usr/local/bundle

ENV PATH=/usr/local/bundle/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV GEM_HOME=/usr/local/bundle

EXPOSE 4567

CMD ["./ruby", "app.rb"]
