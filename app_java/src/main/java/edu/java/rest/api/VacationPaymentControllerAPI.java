package edu.java.rest.api;

import edu.java.rest.model.ApiErrorResponse;
import edu.java.rest.model.PaymentResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import jakarta.validation.Valid;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import java.time.LocalDate;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Validated
@RequestMapping("/calculate")
public interface VacationPaymentControllerAPI {
    @Operation(summary = "Get the payment of provided days of vacation")
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = ("The payment successfully calculated"),
            content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE,
                               schema = @Schema(implementation = PaymentResponse.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Incorrect request parameters",
            content = @Content(mediaType = MediaType.APPLICATION_JSON_VALUE,
                               schema = @Schema(implementation = ApiErrorResponse.class))
        )
    })
    @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    ResponseEntity<PaymentResponse> getPaymentWithParams(
        @RequestParam(name = "average_salary") @Valid @Min(0) double averageSalary,
        @RequestParam(name = "vacation_days") @Valid @Min(0) @Max(365) int vacationDays,
        @RequestParam(name = "vacation_start", required = false) LocalDate vacationStart,
        @RequestParam(name = "vacation_end", required = false) LocalDate vacationEnd
    );
}
