package edu.java.rest.api;

import edu.java.rest.api.exception.IncorrectDatesException;
import edu.java.rest.model.ApiErrorResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class ExceptionApiHandler {
    private static final String INCORRECT_ARGUMENTS = "Provided arguments is incorrect";

    @ExceptionHandler(value = MethodArgumentNotValidException.class)
    public ResponseEntity<ApiErrorResponse> validationFailure(MethodArgumentNotValidException exception) {
        return ResponseEntity.status(exception.getStatusCode())
            .body(
                new ApiErrorResponse(INCORRECT_ARGUMENTS,
                    exception.getStatusCode().toString(), exception.getClass().getName(),
                    exception.getMessage()
                )
            );
    }

    @ExceptionHandler(value = IncorrectDatesException.class)
    public ResponseEntity<ApiErrorResponse> validationFailure(IncorrectDatesException exception) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST)
            .body(
                new ApiErrorResponse(INCORRECT_ARGUMENTS,
                    HttpStatus.BAD_REQUEST.toString(), exception.getClass().getName(),
                    exception.getMessage()
                )
            );
    }
}
