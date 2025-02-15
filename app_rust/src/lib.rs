use actix_web::{get, HttpResponse, Result};
use rand::seq::SliceRandom;
use tera::{Context, Tera};

pub static QUOTES: &[(&str, &str)] = &[
    (
        "The only way to do great work is to love what you do.",
        "Steve Jobs",
    ),
    (
        "Innovation distinguishes between a leader and a follower.",
        "Steve Jobs",
    ),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    (
        "Code is like humor. When you have to explain it, it's bad.",
        "Cory House",
    ),
    (
        "First, solve the problem. Then, write the code.",
        "John Johnson",
    ),
];

#[get("/")]
pub async fn index() -> Result<HttpResponse> {
    let tera = Tera::new("templates/**/*").unwrap();
    let mut context = Context::new();

    let quote = QUOTES.choose(&mut rand::thread_rng()).unwrap();
    context.insert("quote", &quote.0);
    context.insert("author", &quote.1);

    let rendered = tera.render("index.html", &context).unwrap();
    Ok(HttpResponse::Ok().content_type("text/html").body(rendered))
}
