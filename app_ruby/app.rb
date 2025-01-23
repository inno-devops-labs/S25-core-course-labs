# frozen_string_literal: true

require 'sinatra'
require 'tzinfo'

get '/' do
  # Set the timezone to Omsk
  timezone = TZInfo::Timezone.get('Asia/Omsk')

  # Get the current time in Omsk timezone
  omsk_time = timezone.now.strftime('%Y-%m-%d %H:%M:%S')

  # Display the time
  "Current time in Omsk: #{omsk_time}"
end
