package edu.java.rest.api;

import edu.java.rest.model.PaymentResponse;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.reactive.AutoConfigureWebTestClient;
import org.springframework.boot.test.autoconfigure.web.reactive.WebFluxTest;
import org.springframework.http.HttpMethod;
import org.springframework.test.web.reactive.server.WebTestClient;
import static org.assertj.core.api.Assertions.assertThat;

@WebFluxTest
@AutoConfigureWebTestClient
public class VacationPaymentControllerTest {
  @Autowired
  private WebTestClient client;

  @Test
  void givenGetRequest_whenNoParams_thenCorrectHandling() {
    client
        .method(HttpMethod.GET)
        .uri(uriBuilder ->
            uriBuilder
                .path("/calculate")
                .build())
        .exchange()
        .expectStatus().isBadRequest();
  }

  @Test
  void givenGetRequest_whenNoDates_thenCorrectHandling() {
    client
        .method(HttpMethod.GET)
        .uri(uriBuilder ->
            uriBuilder
                .queryParam("average_salary", 12 * 29.3)
                .queryParam("vacation_days", 1)
                .path("/calculate")
                .build())
        .exchange()
        .expectStatus().isOk()
        .expectBody(PaymentResponse.class)
        .value(paymentResponse ->
            assertThat(paymentResponse.getPayment()).isEqualTo(1.0)
        );
  }

  @Test
  void givenGetRequest_whenOnly1Date_thenHandledByVacationDays() {
    client
        .method(HttpMethod.GET)
        .uri(uriBuilder ->
            uriBuilder
                .queryParam("average_salary", 12 * 29.3)
                .queryParam("vacation_days", 1)
                .queryParam("vacation_start", "2024-03-28")
                .path("/calculate")
                .build())
        .exchange()
        .expectStatus().isOk()
        .expectBody(PaymentResponse.class)
        .value(paymentResponse ->
            assertThat(paymentResponse.getPayment()).isEqualTo(1.0)
        );
  }

  @Test
  void givenGetRequest_whenBothDates_thenCorrectHandling() {
    client
        .method(HttpMethod.GET)
        .uri(uriBuilder ->
            uriBuilder
                .queryParam("average_salary", 12 * 29.3)
                .queryParam("vacation_days", 0)
                .queryParam("vacation_start", "2024-03-28")
                .queryParam("vacation_end", "2024-03-30")
                .path("/calculate")
                .build())
        .exchange()
        .expectStatus().isOk()
        .expectBody(PaymentResponse.class)
        .value(paymentResponse ->
            assertThat(paymentResponse.getPayment()).isEqualTo(2.0)
        );
  }
}
