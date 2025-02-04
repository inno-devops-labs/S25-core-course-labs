name := "MoscowTimeApp"

version := "0.1"

scalaVersion := "2.13.10"

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-http" % "10.2.10",
  "com.typesafe.akka" %% "akka-stream" % "2.6.20",
  "com.typesafe.akka" %% "akka-http-spray-json" % "10.2.10",
  "org.scalatest" %% "scalatest" % "3.2.15" % Test

)