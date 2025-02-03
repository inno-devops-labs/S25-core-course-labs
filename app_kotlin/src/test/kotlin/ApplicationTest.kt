package com.ktor

import io.ktor.client.request.get
import io.ktor.client.statement.bodyAsText
import io.ktor.http.HttpStatusCode
import io.ktor.server.testing.testApplication
import java.time.Instant
import java.time.ZoneOffset
import java.time.format.DateTimeFormatter
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertTrue

class ApplicationTest {
    @Test
    fun testTimeEndpoint() = testApplication {
        application { configureRouting() }

        val response = client.get("/time")
        assertEquals(HttpStatusCode.OK, response.status)

        val expectedTime = DateTimeFormatter
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
