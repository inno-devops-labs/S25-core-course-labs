#[macro_use] extern crate rocket;
use rocket::response::content;
use chrono::{Utc, TimeZone};
use chrono::offset::FixedOffset;

#[get("/")]
fn index() -> content::RawHtml<String> {
    // Moscow is UTC+3
    let moscow_time = FixedOffset::east_opt(3 * 3600).expect("REASON").from_utc_datetime(&Utc::now().naive_utc());
    
    // Apply formatting
    let formatted_time = moscow_time.format("%Y-%m-%d %H:%M:%S").to_string();
    
    // Build HTML page
    content::RawHtml(format!("<h1>Current time in Moscow: {}</h1>", formatted_time))
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}

#[cfg(test)]
mod tests {
    use super::*;
    use rocket::local::blocking::Client;
    use regex::Regex;
    use chrono::{Utc, NaiveDateTime, FixedOffset, Timelike};

    // Test 1: Availability Check
    #[test]
    fn test_index_availability() {
        let client = Client::tracked(rocket()).expect("valid rocket instance");
        let response = client.get("/").dispatch();
        assert_eq!(response.status(), rocket::http::Status::Ok);
    }

    // Test 2: HTML Structure Validation
    #[test]
    fn test_html_structure() {
        let client = Client::tracked(rocket()).expect("valid rocket instance");
        let response = client.get("/").dispatch();
        let body = response.into_string().unwrap();
        
        // Verify Moscow keyword presence and time format
        let pattern = r"<h1>Current time in Moscow: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}</h1>";
        assert!(
            Regex::new(pattern).unwrap().is_match(&body),
            "HTML structure validation failed"
        );
    }

    // Test 3: Time Accuracy Check
    #[test]
    fn test_time_accuracy() {
        let client = Client::tracked(rocket()).expect("valid rocket instance");
        
        // Get time bounds around the request (truncated to seconds)
        let before_request = Utc::now().with_nanosecond(0).unwrap();
        let response = client.get("/").dispatch();
        let after_request = Utc::now().with_nanosecond(0).unwrap();

        // Extract displayed time from response
        let body = response.into_string().unwrap();
        let time_match = Regex::new(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
            .unwrap()
            .captures(&body)
            .expect("Time pattern not found")[1]
            .to_string();

        // Parse and convert displayed time to UTC
        let naive_time = NaiveDateTime::parse_from_str(&time_match, "%Y-%m-%d %H:%M:%S")
            .expect("Failed to parse time");
        let moscow_time = FixedOffset::east_opt(3 * 3600)
            .unwrap()
            .from_local_datetime(&naive_time)
            .unwrap()
            .with_timezone(&Utc);

        // Validate time is within truncated test execution window
        assert!(
            moscow_time >= before_request && moscow_time <= after_request,
            "Displayed time {} not in expected range [{} - {}]",
            moscow_time,
            before_request,
            after_request
        );
    }
}
