package com.example

import io.ktor.http.content.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.html.*
import io.ktor.server.http.content.*
import io.ktor.server.netty.*
import io.ktor.server.routing.*
import kotlinx.html.*

fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            static("static") {
                resources("static")
            }
            get("/") {
                val catImages = listOf(
                    "https://avatars.mds.yandex.net/i?id=60d14977ea6c5b526cee98019875a756_l-5242562-images-thumbs&n=13",
                    "https://avatars.mds.yandex.net/i?id=a885e1b648a998e5831aa19e924dae5d_l-9044919-images-thumbs&n=13",
                    "https://i.pinimg.com/736x/81/9b/23/819b2344a30d7ae8724eede289b3a9cd.jpg",
                    "https://i.pinimg.com/736x/91/77/79/917779d9a78e3071ac8266813b513330.jpg",
                    "https://i.ytimg.com/vi/0T-7n9RFd4w/maxresdefault.jpg",
                    "https://i.pinimg.com/originals/e0/d5/01/e0d5015600028364b84fc07ef13827a2.jpg",
                )

                val randomCat = catImages.random()

                call.respondHtml {
                    head {
                        title("Random Cat")
                    }
                    body {
                        h1 { +"Here is a random cat!" }
                        img {
                            src = randomCat
                            alt = "Random Cat"
                        }
                        br
                        a(href = "/") { +"Refresh for a new cat" }
                    }
                }
            }
        }
    }.start(wait = true)
}
