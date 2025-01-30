package com.example

import io.kotest.core.spec.style.DescribeSpec
import io.kotest.matchers.shouldBe
import io.kotest.matchers.string.shouldContain
import io.kotest.matchers.string.shouldMatch
import io.ktor.http.HttpMethod
import io.ktor.http.HttpStatusCode
import io.ktor.server.testing.*

class MainTest : DescribeSpec({
    describe("Ktor Application Tests") {
        it("should return 'Current Time in Moscow:' with a valid date") {
            withTestApplication({ module() }) {
                handleRequest(HttpMethod.Get, "/").apply {
                    response.status() shouldBe HttpStatusCode.OK
                    val content = response.content
                    content shouldContain "Current Time in Moscow:"

                    // Extract the date portion from the response (assuming it's the rest of the content)
                    val dateString = content?.replace("Current Time in Moscow:", "")?.trim()

                    // Add a regex pattern for the date format (yyyy-MM-dd HH:mm:ss)
                    val dateRegex = """\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}""".toRegex()

                    // Check if the date string matches the regex pattern
                    dateString shouldMatch dateRegex
                }
            }
        }
    }
})
