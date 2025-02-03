package com.ktor

import io.ktor.server.application.Application
import io.ktor.server.http.content.staticFiles
import io.ktor.server.response.respondText
import io.ktor.server.routing.get
import io.ktor.server.routing.routing
import java.io.File
import java.time.Instant
import java.time.ZoneOffset
import java.time.format.DateTimeFormatter

fun Application.configureRouting() {
    routing {
        staticFiles("/", File("static"))
        get("/time") {
            val utcTime = DateTimeFormatter
                .ofPattern("HH:mm:ss")
                .withZone(ZoneOffset.UTC)
                .format(Instant.now())
            call.respondText(utcTime)
        }
    }
}
