package com.ktor

import io.ktor.server.application.Application
import io.ktor.server.http.content.defaultResource
import io.ktor.server.http.content.files
import io.ktor.server.http.content.static
import io.ktor.server.http.content.staticRootFolder
import io.ktor.server.response.respondText
import io.ktor.server.routing.get
import io.ktor.server.routing.routing
import io.micrometer.prometheus.PrometheusConfig
import io.micrometer.prometheus.PrometheusMeterRegistry
import java.io.File
import java.time.Instant
import java.time.ZoneOffset
import java.time.format.DateTimeFormatter

fun Application.configureRouting() {
    val prometheusRegistry = PrometheusMeterRegistry(PrometheusConfig.DEFAULT)
    val customCounter = prometheusRegistry.counter("custom_counter")
    routing {
        static("/") {
            staticRootFolder = File("../resources/main")
            defaultResource("index.html")
            files("")
        }
        get("/time") {
            val utcTime = DateTimeFormatter
                .ofPattern("HH:mm:ss")
                .withZone(ZoneOffset.UTC)
                .format(Instant.now())
            customCounter.increment()
            call.respondText(utcTime)
        }
        get("/metrics") {
            call.respondText(
                prometheusRegistry.scrape(),
                contentType = io.ktor.http.ContentType.Text.Plain
            )
        }
    }
}
