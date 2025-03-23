import java.io.File
import java.time.ZoneId
import java.time.ZonedDateTime
import java.time.format.DateTimeFormatter

fun getMoscowTime(): String {
    val moscowZoneId = ZoneId.of("Europe/Moscow")
    val moscowTime = ZonedDateTime.now(moscowZoneId)

    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
    return moscowTime.format(formatter)
}


private val visitsFile = File(System.getenv("VISITS_FILE") ?: "data/visits.txt")

@Suppress("TooGenericExceptionCaught", "SwallowedException")
fun getVisits(): Int {
    return try {
        visitsFile.parentFile?.mkdirs()
        if (visitsFile.exists()) {
            visitsFile.readText().trim().toIntOrNull() ?: 0
        } else {
            0
        }
    } catch (e: Exception) {
        0
    }
}

fun incrementVisits(): Int {
    val visits = getVisits() + 1
    visitsFile.parentFile?.mkdirs()
    visitsFile.writeText(visits.toString())
    return visits
}
