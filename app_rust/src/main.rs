use actix_web::{get, web, App, HttpServer, Responder};
use rand::{rngs::StdRng, RngCore, SeedableRng};
use std::sync::Mutex;

struct AppState {
    rng: Mutex<StdRng>,
}

fn create_html_string(number: u64) -> String {
    format!(
        "
<!doctype html>
<html>
    <head>
        <title>Random unsigned 64-bit integer</title>
    </head>
    <body>
        <p>Your random unsigned 64-bit integer is:</p>
        <p>{number}</p>
    </body>
    <script>
    </script>
</html>
"
    )
}

#[get("/")]
async fn root(state: web::Data<AppState>) -> impl Responder {
    let mut rng = state.rng.lock().unwrap();

    web::Html::new(create_html_string(rng.next_u64()))
}

#[actix_web::main]
async fn main() {
    pretty_env_logger::init();

    let addr = ("127.0.0.1", 8080);
    log::info!("Running server at http://{}:{}", addr.0, addr.1);

    let state = web::Data::new(AppState {
        rng: Mutex::new(StdRng::seed_from_u64(1337u64)),
    });

    let server = match HttpServer::new(move || App::new().app_data(state.clone()).service(root))
        .bind(("127.0.0.1", 8080))
    {
        Ok(server) => server,
        Err(e) => {
            log::error!("Failed to bind to {}:{}: {e}", addr.0, addr.1);
            std::process::exit(1);
        }
    };

    if let Err(e) = server.run().await {
        log::error!("Failed to run server: {e}");
        std::process::exit(1);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn create_html_string_inserts_a_number() {
        let string = create_html_string(20);
        assert!(string.contains("20"));

        let string = create_html_string(1382838);
        assert!(string.contains("1382838"));

        let string = create_html_string(1337);
        assert!(string.contains("1337"));
    }
}
