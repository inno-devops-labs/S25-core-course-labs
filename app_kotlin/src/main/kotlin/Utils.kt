import java.time.ZoneId
import java.time.ZonedDateTime
import java.time.format.DateTimeFormatter

fun getMoscowTime(): String {
    val moscowZoneId = ZoneId.of("Europe/Moscow")
    val moscowTime = ZonedDateTime.now(moscowZoneId)

    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
    return moscowTime.format(formatter)
}
