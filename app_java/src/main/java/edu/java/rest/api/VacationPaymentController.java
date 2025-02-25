package edu.java.rest.api;

import edu.java.rest.api.exception.IncorrectDatesException;
import edu.java.rest.model.PaymentResponse;
import edu.java.rest.model.VisitsResponse;
import edu.java.utils.DateUtils;
import edu.java.utils.PaymentUtils;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.time.LocalDate;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

@RestController
@Slf4j
public class VacationPaymentController implements VacationPaymentControllerAPI {
  private static final String ERROR_FORMATTED = "The provided dates are incorrect: -- {%s} -- {%s}";

  @Override
  public ResponseEntity<PaymentResponse> getPaymentWithParams(
      double averageSalary,
      int vacationDays,
      LocalDate vacationStart,
      LocalDate vacationEnd
  ) {
    getAndIncrement(true);

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

  @Override
  public ResponseEntity<VisitsResponse> getVisits() {
    return ResponseEntity.ok(
        new VisitsResponse(getAndIncrement(false))
    );
  }

  private long getAndIncrement(boolean needIncrement) {
    try {
      Path folder = Path.of(new File("/home/appuser").getAbsolutePath(), "data");
      if (!Files.exists(folder) || !Files.isDirectory(folder)) {
        Files.createDirectories(folder);
      }

      Path visitsFile = folder.resolve("visits");
      if (!Files.exists(visitsFile)) {
        Files.createFile(visitsFile);
        Files.writeString(visitsFile, "0");
      }

      long visits = Long.parseLong(Files.readString(visitsFile));
      log.info("Number of visits is {}", visits);

      if (needIncrement) {
        visits += 1;
        Files.writeString(visitsFile, String.valueOf(visits));
      }

      return visits;
    } catch (Exception e) {
      log.error("Error while creating visits", e);
    }

    throw new RuntimeException();
  }
}
