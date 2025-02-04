import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.ZoneId;
import spark.Spark;

public class OmskTimeApp {
    public static void main(String[] args) {
        // Set the server port
        Spark.port(4567);

        // Define a route for the root URL
        Spark.get("/", (req, res) -> {
            // Get the current time in Omsk timezone
            ZonedDateTime omskTime = ZonedDateTime.now(ZoneId.of("Asia/Omsk"));
            String formattedTime = omskTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));

            // Return an HTML response with the current time
            return "<h1>Time in Omsk</h1><p>" + formattedTime + "</p>";
        });

        // Print a message to indicate the server is running
        System.out.println("Server is running on http://localhost:4567");
    }
}
