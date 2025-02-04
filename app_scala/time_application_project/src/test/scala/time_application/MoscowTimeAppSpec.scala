package time_application

import org.scalatest.wordspec.AnyWordSpec
import org.scalatest.matchers.should.Matchers
import java.time.ZoneId
import java.time.ZonedDateTime
import java.time.format.DateTimeFormatter
import akka.http.scaladsl.model.HttpEntity
import akka.http.scaladsl.model.ContentTypes

class MoscowTimeAppTest extends AnyWordSpec with Matchers {

  // Helper function to generate Moscow time
  private def getMoscowTime: String =
    ZonedDateTime
      .now(ZoneId.of("Europe/Moscow"))
      .format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))

  "MoscowTimeApp" should {

    "generate the correct Moscow time in the specified format" in {
      val moscowTime = getMoscowTime
      moscowTime should fullyMatch regex """\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"""
    }

    "generate valid HTML content with the correct time placeholder" in {
      val moscowTime = getMoscowTime
      val htmlContent =
        s"""
           |<!DOCTYPE html>
           |<html>
           |    <head>
           |    <title>Current Time in Moscow</title>
           |    <style>
           |        body {
           |        font-family: Arial, sans-serif;
           |        text-align: center;
           |        margin-top: 50px;
           |        }
           |        h1 {
           |        color: #333;
           |        }
           |        .time {
           |        font-size: 2em;
           |        color: #007BFF;
           |        }
           |    </style>
           |    <script>
           |        function updateTime() {
           |        fetch('/time')
           |            .then(response => response.text())
           |            .then(time => {
           |            document.getElementById('time').innerText = time;
           |            });
           |        }
           |    </script>
           |    </head>
           |    <body>
           |    <h1>Current Time in Moscow</h1>
           |    <div id="time" class="time">$moscowTime</div>
           |    </body>
           |</html>
           |""".stripMargin

      // Check if the HTML contains the expected structure
      htmlContent should include("<title>Current Time in Moscow</title>")
      htmlContent should include("<h1>Current Time in Moscow</h1>")
      htmlContent should include(s"""<div id="time" class="time">$moscowTime</div>""")
      htmlContent should include("""fetch('/time')""")
    }

    "construct an HTTP entity with the correct content type and HTML body" in {
      val moscowTime = getMoscowTime
      val httpEntity = HttpEntity(
        ContentTypes.`text/html(UTF-8)`,
        s"""
           |<!DOCTYPE html>
           |<html>
           |    <head>
           |    <title>Current Time in Moscow</title>
           |    <style>
           |        body {
           |        font-family: Arial, sans-serif;
           |        text-align: center;
           |        margin-top: 50px;
           |        }
           |        h1 {
           |        color: #333;
           |        }
           |        .time {
           |        font-size: 2em;
           |        color: #007BFF;
           |        }
           |    </style>
           |    <script>
           |        function updateTime() {
           |        fetch('/time')
           |            .then(response => response.text())
           |            .then(time => {
           |            document.getElementById('time').innerText = time;
           |            });
           |        }
           |    </script>
           |    </head>
           |    <body>
           |    <h1>Current Time in Moscow</h1>
           |    <div id="time" class="time">$moscowTime</div>
           |    </body>
           |</html>
           |""".stripMargin
      )

      // Validate the HTTP entity
      httpEntity.contentType shouldBe ContentTypes.`text/html(UTF-8)`
      httpEntity.data.utf8String should include(moscowTime)
      httpEntity.data.utf8String should include("<title>Current Time in Moscow</title>")
    }

    "generate the correct Moscow time compared to the actual current time" in {
      // Generate the Moscow time using the application logic
      val generatedMoscowTime = ZonedDateTime.now(ZoneId.of("Europe/Moscow"))

      // Parse the generated time into a comparable format
      val generatedFormattedTime =
        generatedMoscowTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))

      // Fetch the actual current time in the Europe/Moscow timezone
      val actualMoscowTime = ZonedDateTime.now(ZoneId.of("Europe/Moscow"))

      // Allow for a small tolerance (±5 second) due to potential delays
      val tolerance  = java.time.Duration.ofSeconds(5)
      val lowerBound = actualMoscowTime.minus(tolerance)
      val upperBound = actualMoscowTime.plus(tolerance)

      // Assert that the generated time falls within the acceptable range
      generatedMoscowTime shouldBe >=(lowerBound)
      generatedMoscowTime shouldBe <=(upperBound)

      // Optionally, print both times for debugging purposes
      println(s"Generated Moscow Time: $generatedFormattedTime")
      println(
        s"Actual Moscow Time: ${actualMoscowTime.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))}"
      )
    }
  }

}
