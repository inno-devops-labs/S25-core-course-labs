#[macro_use] extern crate rocket;
#[macro_use] extern crate lazy_static;

use rocket::response::content;
use rocket::tokio::fs::File;
use rocket::tokio::io::{self, AsyncReadExt, AsyncWriteExt};
use chrono::{Utc, TimeZone, FixedOffset};
use prometheus::{Registry, Counter, TextEncoder, Encoder};

// Create metrics registry and register metrics
lazy_static! {
    static ref REGISTRY: Registry = Registry::new();
    static ref REQUEST_COUNTER: Counter = {
        let counter = Counter::new(
            "app_http_requests_total",
            "Total HTTP Requests"
        ).expect("Failed to create counter");
        REGISTRY.register(Box::new(counter.clone())).expect("Failed to register counter");
        counter
    };
}

const VISITS_FILE: &str = "visits.txt";

// Function to read the current number of visits from the file
async fn read_visits() -> io::Result<u64> {
    match File::open(VISITS_FILE).await {
        Ok(mut file) => {
            let mut contents = String::new();
            file.read_to_string(&mut contents).await?;
            // Parse the file contents to u64, defaulting to 0 if empty or invalid
            match contents.trim().parse::<u64>() {
                Ok(visits) => Ok(visits),
                Err(_) => Ok(0), // Return 0 if parsing fails
            }
        },
        Err(_) => {
            // Create the file if it doesn't exist and initialize the visits count
            let mut file = File::create(VISITS_FILE).await?;
            file.write_all(b"0").await?; // Initialize with "0"
            Ok(0) // Return 0 since it was a new file
        }
    }
}

// Function to update the visit counter in the file
async fn update_visits(count: u64) -> io::Result<()> {
    let mut file = File::create(VISITS_FILE).await?;
    file.write_all(count.to_string().as_bytes()).await?;
    Ok(())
}

#[get("/")]
async fn index() -> content::RawHtml<String> {
    REQUEST_COUNTER.inc();
    
    // Increment the visit counter
    let current_visits = read_visits().await.unwrap_or(0);
    let updated_visits = current_visits + 1;
    update_visits(updated_visits).await.unwrap();

    // Get the current time in Moscow
    let moscow_time = FixedOffset::east_opt(3 * 3600)
        .expect("Invalid offset")
        .from_utc_datetime(&Utc::now().naive_utc());
    
    let formatted_time = moscow_time.format("%Y-%m-%d %H:%M:%S").to_string();
    content::RawHtml(format!("<h1>Current time in Moscow: {}</h1>", formatted_time))
}

#[get("/visits")]
async fn visits() -> content::RawHtml<String> {
    let visits_count = read_visits().await.unwrap_or(0);
    content::RawHtml(format!("<h1>Total Visits: {}</h1>", visits_count))
}

#[get("/metrics")]
fn metrics() -> String {
    let encoder = TextEncoder::new();
    let metric_families = REGISTRY.gather();
    let mut buffer = Vec::new();
    encoder.encode(&metric_families, &mut buffer).unwrap();
    String::from_utf8(buffer).unwrap()
}

#[get("/health")]
fn health() -> &'static str {
    "OK"
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/", routes![index, metrics, health, visits])
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
