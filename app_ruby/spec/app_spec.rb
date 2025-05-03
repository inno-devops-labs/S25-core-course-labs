# frozen_string_literal: true

require 'rack/test'
require './app'

describe 'Omsk Time Web App' do
  include Rack::Test::Methods

  def app
    Sinatra::Application
  end

  it 'displays the current time in Omsk' do
    header 'Host', 'localhost'
    get '/'
    expect(last_response).to be_ok
    expect(last_response.body).to include('Current time in Omsk')
  end
end
