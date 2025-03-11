use actix_web::{test, App};
use quote_app::*; // assuming we'll move our main app logic to lib.rs

#[actix_web::test]
async fn test_get_quote() {
    // Create test app
    let app = test::init_service(App::new().service(index)).await;

    // Create test request
    let req = test::TestRequest::get().uri("/").to_request();

    // Perform the request and get response
    let resp = test::call_service(&app, req).await;

    // Assert response status
    assert!(resp.status().is_success());

    // Get response body
    let body = test::read_body(resp).await;
    let body_str = String::from_utf8(body.to_vec()).unwrap();

    // Assert response contains expected elements
    assert!(body_str.contains("quote-container"));
    assert!(body_str.contains("quote"));
    assert!(body_str.contains("author"));
    assert!(
        body_str.contains("Steve Jobs")
            || body_str.contains("Cory House")
            || body_str.contains("John Johnson")
    );
}

#[actix_web::test]
async fn test_response_content_type() {
    let app = test::init_service(App::new().service(index)).await;
    let req = test::TestRequest::get().uri("/").to_request();
    let resp = test::call_service(&app, req).await;

    assert_eq!(
        resp.headers()
            .get("content-type")
            .unwrap()
            .to_str()
            .unwrap(),
        "text/html"
    );
}

#[actix_web::test]
async fn test_template_rendering() {
    let app = test::init_service(App::new().service(index)).await;
    let req = test::TestRequest::get().uri("/").to_request();
    let resp = test::call_service(&app, req).await;
    let body = test::read_body(resp).await;
    let body_str = String::from_utf8(body.to_vec()).unwrap();

    // Check for template elements
    assert!(body_str.contains("Refresh the page for a new quote"));
    assert!(body_str.contains(r#"class="quote-container""#));
    assert!(body_str.contains(r#"class="quote""#));
    assert!(body_str.contains(r#"class="author""#));
}
