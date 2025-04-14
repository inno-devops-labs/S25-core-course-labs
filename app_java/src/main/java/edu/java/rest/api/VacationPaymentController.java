package edu.java.rest.api;

import edu.java.rest.api.exception.IncorrectDatesException;
import edu.java.rest.model.PaymentResponse;
import edu.java.utils.DateUtils;
import edu.java.utils.PaymentUtils;
import java.time.LocalDate;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class VacationPaymentController implements VacationPaymentControllerAPI {
    private static final String ERROR_FORMATTED = "The provided dates are incorrect: -- {%s} -- {%s}";

    @Override
    public ResponseEntity<PaymentResponse> getPaymentWithParams(
        double averageSalary,
        int vacationDays,
        LocalDate vacationStart,
        LocalDate vacationEnd
    ) {
        if (DateUtils.isStartEndDateProvided(vacationStart, vacationEnd)) {
            if (!DateUtils.isCorrectStartEndDate(vacationStart, vacationEnd)) {
                throw new IncorrectDatesException(
                    String.format(ERROR_FORMATTED, vacationStart, vacationEnd)
                );
            }

            return ResponseEntity.ok(new PaymentResponse(
                PaymentUtils.calculatePayment(
                    averageSalary,
                    DateUtils.daysBetweenExcludingWeekends(vacationStart, vacationEnd)
                )
            ));
        }

        return ResponseEntity.ok(new PaymentResponse(
            PaymentUtils.calculatePayment(averageSalary, vacationDays)
        ));
    }
}
