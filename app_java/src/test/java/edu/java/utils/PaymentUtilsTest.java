package edu.java.utils;

import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class PaymentUtilsTest {
    @Test
    void given1Values_thenCorrectCalculation() {
        assertThat(PaymentUtils.calculatePayment(10000, 10))
            .isEqualTo(10000.0 / 12 / 29.3 * 10);
    }

    @Test
    void given2Values_thenCorrectCalculation() {
        assertThat(PaymentUtils.calculatePayment(23500, 10))
            .isEqualTo(23500.0 / 12 / 29.3 * 10);
    }
}
