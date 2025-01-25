package com.ktor

import io.ktor.server.application.*
import io.ktor.server.http.content.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import java.time.Instant
import java.time.ZoneOffset
import java.time.format.DateTimeFormatter

fun Application.configureRouting() {
    routing {
        static("/") {
            resources("")
            defaultResource("index.html")
        }
        get("/time") {
            val utcTime = DateTimeFormatter
                .ofPattern("HH:mm:ss")
                .withZone(ZoneOffset.UTC)
                .format(Instant.now())
            call.respondText(utcTime)
        }
    }
}
