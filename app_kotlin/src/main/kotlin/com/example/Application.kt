package com.example

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.metrics.micrometer.*
import io.ktor.server.netty.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import io.micrometer.core.instrument.binder.jvm.JvmGcMetrics
import io.micrometer.core.instrument.binder.jvm.JvmMemoryMetrics
import io.micrometer.core.instrument.binder.system.ProcessorMetrics
import io.micrometer.core.instrument.distribution.DistributionStatisticConfig
import io.micrometer.prometheus.PrometheusConfig
import io.micrometer.prometheus.PrometheusMeterRegistry
import okio.FileSystem
import okio.IOException
import okio.Path
import okio.Path.Companion.toPath
import java.text.SimpleDateFormat
import java.time.Duration
import java.util.*

val path: Path = "/data/counter".toPath()

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module).start(wait = true)
}

fun updateCounter() {
    try {
        val temp = FileSystem.SYSTEM.read(path) { readUtf8() }
        val value = temp.toIntOrNull() ?: 0
        FileSystem.SYSTEM.write(path) { writeUtf8("${value + 1}") }
    } catch (e: IOException) {
        // Если файла нет или ошибка чтения, создаем с нуля
        FileSystem.SYSTEM.write(path) { writeUtf8("1") }
    }
}

fun getMoscowTime(): String {
    val moscowTimeZone = TimeZone.getTimeZone("Europe/Moscow")
    val dateFormat = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
    dateFormat.timeZone = moscowTimeZone
    return dateFormat.format(Date())
}

fun Application.module() {
    try {
        if (!FileSystem.SYSTEM.exists(path)) {
            FileSystem.SYSTEM.write(path) { writeUtf8("0") }
        }
    } catch (e: IOException) {
        log.error("Ошибка при инициализации счетчика", e)
    }

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

    routing {
        get("/") {
            updateCounter()
            val moscowTime = getMoscowTime()
            call.respondText("Current Time in Moscow: $moscowTime")
        }

        get("/metrics") {
            call.respond(appMicrometerRegistry.scrape())
        }

        get("/visited") {
            updateCounter()
            val count = try {
                FileSystem.SYSTEM.read(path) { readUtf8() }.toIntOrNull() ?: 0
            } catch (e: IOException) {
                0
            }
            call.respondText("Visited: $count")
        }
    }
}
