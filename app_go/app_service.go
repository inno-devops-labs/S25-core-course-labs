package main

import (
	"time"
)

// returns the current time in the default timezone.
func get_time() string {
	const defaultTimezone = "Europe/Moscow"
	return get_tz_time(defaultTimezone)
}

// get_tz_time returns the current time in the specified timezone.
// param timezone: The timezone to get the current time from.
func get_tz_time(timezone string) string {
	const timeFormat = "15:04 (03:04 PM)"
	location, err := time.LoadLocation(timezone)
	if err != nil {
		location = time.UTC
	}
	return time.Now().In(location).Format(timeFormat)
}
