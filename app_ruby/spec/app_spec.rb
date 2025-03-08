# frozen_string_literal: true

require 'rack/test'
require './app'

describe 'Omsk Time Web App - Basic Responses' do
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  describe 'GET /' do
    it 'responds successfully' do
      header 'Host', 'localhost'
      get '/'
      expect(last_response).to be_ok
    end

    it 'displays the current time in Omsk' do
      header 'Host', 'localhost'
      get '/'
      expect(last_response.body).to match(/Current time in Omsk: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/)
    end

    it 'returns text/plain content type' do
      header 'Host', 'localhost'
      get '/'
      expect(last_response.headers['Content-Type']).to include('text/plain')
    end
  end
end

describe 'Omsk Time Web App - Error Handling' do
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  it 'handles invalid timezone errors gracefully' do
    allow(TZInfo::Timezone).to receive(:get).and_raise(TZInfo::InvalidTimezoneIdentifier, 'Invalid timezone')

    header 'Host', 'localhost'
    get '/'

    expect(last_response).to be_ok
    expect(last_response.body).to include('Error: Invalid timezone identifier - Invalid timezone')
  end

  it 'handles unexpected errors gracefully' do
    allow(TZInfo::Timezone).to receive(:get).and_raise(StandardError, 'Unexpected error')

    header 'Host', 'localhost'
    get '/'

    expect(last_response).to be_ok
    expect(last_response.body).to include('Error: Unexpected error')
  end
end

describe 'Omsk Time Web App - Time Format' do
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  it 'displays time in YYYY-MM-DD HH:MM:SS format' do
    header 'Host', 'localhost'
    get '/'
    expect(last_response.body).to match(/\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/)
  end
end
