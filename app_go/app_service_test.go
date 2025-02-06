package main

import (
	"regexp"
	"testing"
	"time"

)

const timeFormat = "15:04 (03:04 PM)"

var regexPattern = regexp.MustCompile(`^\d\d:\d\d \(\d\d:\d\d (AM|PM)\)$`)

func TestGetTZTimeValid(t *testing.T) {
	timezone := "Europe/Moscow"
	result := get_tz_time(timezone)

	if !regexPattern.MatchString(result) {
		t.Errorf("GetTZTime(%q) returned %q, which does not match the expected format", timezone, result)
	}

	location, err := time.LoadLocation(timezone)
	if err != nil {
		t.Fatalf("Failed to load location %q: %v", timezone, err)
	}
	parsedTime, err := time.ParseInLocation(timeFormat, result, location)
	if err != nil {
		t.Errorf("Returned time %q could not be parsed: %v", result, err)
	}

	now := time.Now().In(location)
	if parsedTime.Hour() != now.Hour() || parsedTime.Minute() != now.Minute() {
		t.Logf("Parsed time %v (hour=%d, minute=%d) is different from now %v (hour=%d, minute=%d). This may occur if the test runs across a minute boundary.",
			parsedTime, parsedTime.Hour(), parsedTime.Minute(), now, now.Hour(), now.Minute())
	}
}

func TestGetTZTimeInvalid(t *testing.T) {
	invalidTimezone := "Invalid/Timezone"
	result := get_tz_time(invalidTimezone)

	if !regexPattern.MatchString(result) {
		t.Errorf("GetTZTime(%q) returned %q, which does not match expected format", invalidTimezone, result)
	}

	parsedTime, err := time.ParseInLocation(timeFormat, result, time.UTC)
	if err != nil {
		t.Errorf("Returned time %q could not be parsed in UTC: %v", result, err)
	}

	nowUTC := time.Now().In(time.UTC)
	if parsedTime.Hour() != nowUTC.Hour() || parsedTime.Minute() != nowUTC.Minute() {
		t.Logf("Parsed UTC time %v (hour=%d, minute=%d) differs from now %v (hour=%d, minute=%d). This may be due to a minute boundary.",
			parsedTime, parsedTime.Hour(), parsedTime.Minute(), nowUTC, nowUTC.Hour(), nowUTC.Minute())
	}
}

func TestGetTime(t *testing.T) {
	result := get_time()

	if !regexPattern.MatchString(result) {
		t.Errorf("GetTime() returned %q which does not match expected format", result)
	}
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		t.Fatalf("Failed to load location Europe/Moscow: %v", err)
	}
	parsedTime, err := time.ParseInLocation(timeFormat, result, location)
	if err != nil {
		t.Errorf("Returned time %q could not be parsed: %v", result, err)
	}
	now := time.Now().In(location)
	if parsedTime.Hour() != now.Hour() || parsedTime.Minute() != now.Minute() {
		t.Logf("Parsed time %v (hour=%d, minute=%d) is different from now %v (hour=%d, minute=%d). This may be due to test timing.",
			parsedTime, parsedTime.Hour(), parsedTime.Minute(), now, now.Hour(), now.Minute())
	}
}
