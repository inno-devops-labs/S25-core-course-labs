# frozen_string_literal: true

require './app'

# Configure Rack directly
use Rack::Protection, except: [:host_authorization, :json_csrf]

# Run the application
run Sinatra::Application
