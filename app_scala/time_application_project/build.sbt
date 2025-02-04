name := "MoscowTimeApp"

version := "0.1"

scalaVersion := "2.13.10"

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-http"            % "10.5.3",
  "com.typesafe.akka" %% "akka-stream"          % "2.7.0",
  "com.typesafe.akka" %% "akka-http-spray-json" % "10.5.3",
  "org.scalatest"     %% "scalatest"            % "3.2.15" % Test
)
