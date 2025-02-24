package edu.java.utils;

import java.time.LocalDate;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.assertThat;

public class DateUtilsTest {
    @Test
    void givenNullArray_thenFalse() {
        assertThat(DateUtils.isStartEndDateProvided(null, null)).isFalse();
    }

    @Test
    void givenTwoDates_thenTrue() {
        assertThat(DateUtils.isStartEndDateProvided(LocalDate.now(), LocalDate.now())).isTrue();
    }

    @Test
    void givenDates_whenStartIsAfterEnd_thenFalse() {
        assertThat(
            DateUtils.isCorrectStartEndDate(
                LocalDate.parse("2024-03-28"),
                LocalDate.parse("2024-03-25")
            )
        ).isFalse();
    }

    @Test
    void givenDates_whenStartIsBeforeEnd_thenTrue() {
        assertThat(
            DateUtils.isCorrectStartEndDate(
                LocalDate.parse("2024-03-28"),
                LocalDate.parse("2024-03-30")
            )
        ).isTrue();
    }

    @Test
    void givenDates_whenYearIsNotCorrect_thenFalse() {
        assertThat(
            DateUtils.isCorrectStartEndDate(
                LocalDate.parse("2022-03-28"),
                LocalDate.parse("2024-03-30")
            )
        ).isFalse();
    }

    @Test
    void givenDates_whenStartIsAfterEnd_thenZeroDays() {
        assertThat(
            DateUtils.daysBetweenExcludingWeekends(
                LocalDate.parse("2024-03-25"),
                LocalDate.parse("2024-03-20")
            )
        ).isEqualTo(0);
    }

    @Test
    void givenDates_whenAllCorrect_thenCertainDays() {
        assertThat(
            DateUtils.daysBetweenExcludingWeekends(
                LocalDate.parse("2024-03-28"),
                LocalDate.parse("2024-04-04")
            )
        ).isEqualTo(5);
    }
}
