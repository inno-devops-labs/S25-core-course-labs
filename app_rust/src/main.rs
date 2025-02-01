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

    #[test]
    fn test_index_status() {
        let rocket = rocket();
        let client = Client::tracked(rocket).expect("valid rocket instance");
        let response = client.get("/").dispatch();
        assert_eq!(response.status(), rocket::http::Status::Ok);
    }

    #[test]
    fn test_index_body_format() {
        let rocket = rocket();
        let client = Client::tracked(rocket).expect("valid rocket instance");
        let response = client.get("/").dispatch();
        let body = response.into_string().expect("response body");
        
        // Ensure the response follows expected HTML format
        let re = Regex::new(r"<h1>Current time in Moscow: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}</h1>").unwrap();
        assert!(re.is_match(&body), "Response body does not match expected format: {}", body);
    }
}
