use actix_web::{App, HttpServer};
use quote_app::index;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    println!("Server running at http://localhost:8080 Enjoy!");
    HttpServer::new(|| App::new().service(index))
        .bind("0.0.0.0:8080")?
        .run()
        .await
}
