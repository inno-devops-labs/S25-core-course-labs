FROM ruby:3.4.1-alpine3.21

ENV BUNDLE_WITHOUT=development:test \
    LANG=C.UTF-8

# Install system dependencies
RUN apk add --no-cache \
        gcc=14.2.0-r4 \
        musl-dev=1.2.5-r8 \
        tzdata=2024b-r1 \
        make=4.4.1-r2

RUN addgroup -S appgroup && \
    adduser -S -G appgroup appuser

WORKDIR /app

RUN gem install nio4r:2.7.4 -- --use-system-libraries && \
    gem install bundler:2.6.3

COPY Gemfile Gemfile.lock ./

RUN bundle install

COPY public/styles.css views/index.erb app.rb config.ru ./

USER appuser

EXPOSE 4567

CMD ["ruby", "app.rb"]
