package time_application

// Imports
import akka.actor.ActorSystem
import akka.http.scaladsl.Http
import akka.http.scaladsl.server.Directives._
import akka.http.scaladsl.model.ContentTypes
import java.time.ZoneId
import java.time.ZonedDateTime
import java.time.format.DateTimeFormatter
import scala.concurrent.Future
import scala.util.{Success, Failure}
import scala.concurrent.Await
import scala.concurrent.duration._
import java.io.{File, PrintWriter}
import scala.io.Source

// Main object
object MoscowTimeApp extends App {

  implicit val system = ActorSystem("MoscowTimeSystem")
  import system.dispatcher

  // File handling for visits
  val visitsDir = new File("./data")
  visitsDir.mkdirs()
  val visitsFile = new File(visitsDir, "visits")

  def getVisits(): Int =
    try
      Source.fromFile(visitsFile).mkString.trim.toInt
    catch {
      case _: Exception => 0
    }

  def incrementVisits(): Int = {
    val count  = getVisits() + 1
    val writer = new PrintWriter(visitsFile)
    writer.write(count.toString)
    writer.close()
    count
  }

  // Route to handle GET requests
  val route =
    path("") {
      get {
        incrementVisits()

        // Current time in Moscow
        val moscowTime = ZonedDateTime
          .now(ZoneId.of("Europe/Moscow"))
          .format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))

        // Return an HTML response
        complete(
          akka.http.scaladsl.model.HttpEntity(
            ContentTypes.`text/html(UTF-8)`,
            s"""
            <!DOCTYPE html>
            <html>
                <head>
                <title>Current Time in Moscow</title>
                <style>
                    body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    }
                    h1 {
                    color: #333;
                    }
                    .time {
                    font-size: 2em;
                    color: #007BFF;
                    }
                </style>
                <script>
                    function updateTime() {
                    fetch('/time')
                        .then(response => response.text())
                        .then(time => {
                        document.getElementById('time').innerText = time;
                        });
                    }
                </script>
                </head>
                <body>
                <h1>Current Time in Moscow</h1>
                <div id="time" class="time">$moscowTime</div>
                </body>
            </html>
            """
          )
        )
      }
    } ~
      path("visits") {
        get {
          complete(
            akka.http.scaladsl.model.HttpEntity(
              ContentTypes.`text/plain(UTF-8)`,
              s"Total visits: ${getVisits()}"
            )
          )
        }
      }

  // Start the server
  val bindingFuture = Http().newServerAt("0.0.0.0", 9090).bind(route)

  bindingFuture.onComplete {
    case Success(binding) =>
      println(s"Server online at http://0.0.0.0:9090/")

      // Add a handle to shut down the server on Ctrl+C
      sys.addShutdownHook {
        binding.unbind().onComplete { _ =>
          system.terminate()
          println("Server stopped.")
        }
      }
    case Failure(ex) =>
      println(s"Failed to bind to port 9090: ${ex.getMessage}")
      system.terminate()
  }

  // Block the main thread to keep the server running
  Await.result(system.whenTerminated, Duration.Inf)

}
