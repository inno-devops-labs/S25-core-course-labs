package ru.nai1ka

import io.ktor.server.application.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import ru.nai1ka.getMoscowTime

fun Application.configureRouting() {
    routing {
        get("/") {
            call.respondText(getMoscowTime())
        }
    }
}
