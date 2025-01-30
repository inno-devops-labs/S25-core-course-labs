use actix_web::{web, App, HttpServer, Responder, HttpResponse};
use chrono::prelude::*;

async fn show_time() -> impl Responder {
    let moscow_time = Utc::now().with_timezone(&FixedOffset::east(3 * 3600));
    HttpResponse::Ok().body(format!("<h1>Current Time in Moscow: {}</h1>", moscow_time))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/", web::get().to(show_time)))
        .bind("127.0.0.1:8080")?
        .run()
        .await
}

