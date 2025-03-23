# frozen_string_literal: true

require 'sinatra'
require 'tzinfo'
require 'prometheus/client'
require 'prometheus/client/formats/text'

VISITS_FILE = '/tmp/visits'

def read_visits
  File.exist?(VISITS_FILE) ? File.read(VISITS_FILE).to_i : 0
end

def increment_visits
  visits = read_visits + 1
  File.write(VISITS_FILE, visits)
  visits
end

# Explicitly set trusted_hosts to allow Prometheus and local connections
set :protection, except: [:json_csrf]
set :bind, '0.0.0.0'
set :environment, :production

# Allow access from any host
use Rack::Protection::HostAuthorization,
    trusted_hosts: [/^localhost$/, /^127\.0\.0\.1$/, /^.+\.monitoring$/, /^omsk-time-app$/, /^prometheus$/, /.*/, nil]

# Initialize Prometheus registry and metrics
prometheus = Prometheus::Client.registry

# Define metrics
http_requests_total = Prometheus::Client::Counter.new(
  :http_requests_total,
  docstring: 'Total number of HTTP requests',
  labels: %i[method path status]
)

http_request_duration_seconds = Prometheus::Client::Histogram.new(
  :http_request_duration_seconds,
  docstring: 'HTTP request duration in seconds',
  labels: %i[method path]
)

timezone_lookup_errors = Prometheus::Client::Counter.new(
  :timezone_lookup_errors_total,
  docstring: 'Total number of timezone lookup errors'
)

# Register metrics
prometheus.register(http_requests_total)
prometheus.register(http_request_duration_seconds)
prometheus.register(timezone_lookup_errors)

# Middleware to track request metrics
before do
  @start_time = Time.now
end

after do
  duration = Time.now - @start_time
  http_requests_total.increment(labels: { method: request.request_method, path: request.path, status: response.status })
  http_request_duration_seconds.observe(duration, labels: { method: request.request_method, path: request.path })
end

get '/' do
  content_type 'text/plain'
  visits = increment_visits

  # Set the timezone to Omsk
  begin
    timezone = TZInfo::Timezone.get('Asia/Omsk')

    # Get the current time in Omsk timezone
    omsk_time = timezone.now.strftime('%Y-%m-%d %H:%M:%S')

    # Display the time and visit count
    "Current time in Omsk: #{omsk_time}\nTotal visits: #{visits}"
  rescue TZInfo::InvalidTimezoneIdentifier => e
    timezone_lookup_errors.increment
    "Error: Invalid timezone identifier - #{e.message}"
  rescue StandardError => e
    timezone_lookup_errors.increment
    "Error: #{e.message}"
  end
end

# Endpoint to get visit count
get '/visits' do
  content_type 'text/plain'
  "Total visits: #{read_visits}"
end

# Prometheus metrics endpoint with explicit host check bypass
get '/metrics' do
  # Skip host protection for the metrics endpoint
  env['rack.protection.host_authorization'] = true

  # Set the content type with explicit charset parameter
  content_type 'text/plain; version=0.0.4; charset=utf-8'

  # Marshal the metrics
  Prometheus::Client::Formats::Text.marshal(prometheus)
end

get '/healthz' do
  status 200
  'OK'
end

get '/ready' do
  status 200
  'Ready'
end
