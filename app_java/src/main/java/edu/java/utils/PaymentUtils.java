package edu.java.utils;

import jakarta.validation.constraints.Min;

public final class PaymentUtils {
    private PaymentUtils() {
    }

    private static final int MONTHS = 12;
    private static final double AVERAGE_WORKING_DAYS_MONTHLY = 29.3;

    public static double calculatePayment(@Min(0) double avgSalary, @Min(0) int vacationDays) {
        return avgSalary / (MONTHS * AVERAGE_WORKING_DAYS_MONTHLY) * vacationDays;
    }
}
