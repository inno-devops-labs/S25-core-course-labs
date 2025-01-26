package edu.java.utils;

import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;
import java.time.LocalDate;
import java.util.Calendar;

public final class DateUtils {
    private DateUtils() {
    }

    public static boolean isStartEndDateProvided(@NotNull @NotEmpty LocalDate... dates) {
        for (var date : dates) {
            if (date == null) {
                return false;
            }
        }
        return true;
    }

    public static boolean isCorrectStartEndDate(LocalDate startDate, LocalDate endDate) {
        return startDate.isBefore(endDate) && (startDate.getYear() == endDate.getYear()
                                               || startDate.getYear() + 1 == endDate.getYear());
    }

    public static int daysBetweenExcludingWeekends(LocalDate startDate, LocalDate endDate) {
        Calendar startCalendar = parseCalendarFromLocalDate(startDate);
        Calendar endCalendar = parseCalendarFromLocalDate(endDate);

        int vacationDays = 0;
        while (startCalendar.before(endCalendar) || startCalendar.equals(endCalendar)) {
            int dayOfWeek = startCalendar.get(Calendar.DAY_OF_WEEK);

            if (!isWeekend(dayOfWeek)) {
                vacationDays++;
            }

            startCalendar.add(Calendar.DAY_OF_MONTH, 1);
        }

        return vacationDays;
    }

    private static Calendar parseCalendarFromLocalDate(LocalDate date) {
        Calendar calendar = Calendar.getInstance();
        calendar.set(date.getYear(), date.getMonthValue(), date.getDayOfMonth());
        return calendar;
    }

    private static boolean isWeekend(int dayOfWeek) {
        return dayOfWeek == Calendar.SATURDAY || dayOfWeek == Calendar.SUNDAY;
    }
}
