package com.ktor

import io.ktor.http.ContentType
import io.ktor.server.application.Application
import io.ktor.server.http.content.resources
import io.ktor.server.http.content.static
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
    val dataDir = File("/data").apply { mkdirs() }
    routing {
        static("/static") {
            resources("static")
        }
        get("/") {
            val file = File(dataDir, "access_count.txt")
            synchronized(dataDir) {
                try {
                    val count = if (file.exists()) file.readText().trim().toInt() else 0
                    file.writeText("${count + 1}")
                } catch (e: Exception) {
                    println(e.message)
                }
            }
            call.respondText(
                this::class.java.classLoader.getResource("index.html")!!.readText(),
                contentType = ContentType.Text.Html
            )
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
        get("/visits") {
            val count = try {
                File("/data/access_count.txt").readText().trim().toInt()
            } catch (e: Exception) {
                0
            }
            call.respondText("Total visits: $count")
        }
    }
}
