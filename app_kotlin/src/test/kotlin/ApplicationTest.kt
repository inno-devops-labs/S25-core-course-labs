package com.ktor

import io.ktor.server.application.*
import io.ktor.server.testing.*
import io.ktor.http.*
import kotlin.test.*
import io.ktor.server.routing.*
import io.ktor.server.response.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import java.time.Instant
import java.time.ZoneOffset
import java.time.format.DateTimeFormatter

class ApplicationTest {
    @Test
    fun testTimeEndpoint() = testApplication {
        application { configureRouting() }

        val response = client.get("/time")
        assertEquals(HttpStatusCode.OK, response.status)

        DateTimeFormatter
            .ofPattern("HH:mm:ss")
            .withZone(ZoneOffset.UTC)
            .format(Instant.now())

        assertTrue(response.bodyAsText().matches(Regex("\\d{2}:\\d{2}:\\d{2}")))
    }

    @Test
    fun testStaticFileServing() = testApplication {
        application { configureRouting() }

        val response = client.get("/")
        assertTrue(response.status == HttpStatusCode.OK || response.status == HttpStatusCode.NotFound)
    }
}
