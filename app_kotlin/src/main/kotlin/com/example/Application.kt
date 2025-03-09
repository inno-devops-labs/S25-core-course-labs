package com.example

import io.ktor.server.application.Application
import io.ktor.server.application.call
import io.ktor.server.engine.embeddedServer
import io.ktor.server.netty.Netty
import io.ktor.server.response.respondText
import io.ktor.server.routing.get
import io.ktor.server.routing.routing
import java.text.SimpleDateFormat
import java.util.Date
import java.util.TimeZone
import io.ktor.server.metrics.micrometer.*
import okio.FileSystem
import okio.IOException
import okio.Path
import okio.Path.Companion.toPath

val path = "/data/counter".toPath()

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module) {
        install(MicrometerMetrics)
    }.start(wait = true)
}

fun update() {
    val temp = FileSystem.SYSTEM.read(path) {readUtf8()}
    val value = temp.toInt()
    FileSystem.SYSTEM.write(path) {writeUtf8("${value+1}")}
}

fun getMoscowTime(): String {
    val moscowTimeZone = TimeZone.getTimeZone("Europe/Moscow")
    val dateFormat = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
    dateFormat.timeZone = moscowTimeZone
    val currentTime = Date()
    return dateFormat.format(currentTime)
}

fun Application.module() {
    FileSystem.SYSTEM.write(path) {writeUtf8("0")}
    val appMicrometerRegistry = PrometheusMeterRegistry(PrometheusConfig.DEFAULT)
    install(MicrometerMetrics) {
        registry = appMicrometerRegistry
        distributionStatisticConfig = DistributionStatisticConfig.Builder()
            .percentilesHistogram(true)
            .maximumExpectedValue(Duration.ofSeconds(20).toNanos().toDouble())
            .serviceLevelObjectives(
                Duration.ofMillis(100).toNanos().toDouble(),
                Duration.ofMillis(500).toNanos().toDouble()
            )
            .build()
        meterBinders = listOf(
            JvmMemoryMetrics(),
            JvmGcMetrics(),
            ProcessorMetrics()
        )
    }
    val counter = 0
    routing {
        get("/") {
            update()
            val moscowTime = getMoscowTime()
            call.respondText("Current Time in Moscow:$moscowTime")
        }
        get("/metrics") {
            update()
            call.respond(appMicrometerRegistry.scrape())
        }
        get("/visited"){
            update()
            val temp = FileSystem.SYSTEM.read(path) {readUtf8()}
            val value = temp.toInt()
            call.respondText(value)
        }
    }
}
