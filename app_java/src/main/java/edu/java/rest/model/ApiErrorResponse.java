package edu.java.rest.model;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import jakarta.validation.constraints.NotBlank;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Getter
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public final class ApiErrorResponse {
    @NotBlank
    private final String description;
    @NotBlank
    private final String code;
    @NotBlank
    private final String exceptionName;
    @NotBlank
    private final String exceptionMessage;
}
