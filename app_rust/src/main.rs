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
