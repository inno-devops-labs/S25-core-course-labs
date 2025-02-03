import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.ZoneId;

public class TestOmskTimeApp {
    @Test
    public void testTimeFormat() {
        ZonedDateTime omskTime = ZonedDateTime.now(ZoneId.of("Asia/Omsk"));
        String formattedTime = omskTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        assertTrue(formattedTime.matches("\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}"));
    }
}
