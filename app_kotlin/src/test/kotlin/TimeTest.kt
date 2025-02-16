import io.ktor.client.request.get
import io.ktor.client.statement.bodyAsText
import io.ktor.http.HttpStatusCode
import io.ktor.server.testing.testApplication
import junit.framework.TestCase.assertEquals
import org.junit.Assert.assertNotEquals
import kotlin.test.Test
import kotlin.test.assertTrue

class TimeTest {
    @Test
    fun `WHEN request to root THEN returns time`() = testApplication {
        application {
            module()
        }

        val response = client.get("/")
        assertEquals(HttpStatusCode.OK, response.status)
        val content = response.bodyAsText()
        assertTrue(content.isNotBlank(), "Response should not be blank")
    }

    @Test
    fun `WHEN request to root THEN time updates`() = testApplication {
        application {
            module()
        }
        val client = createClient { }
        val firstResponse = client.get("/").bodyAsText()
        Thread.sleep(1000)
        val secondResponse = client.get("/").bodyAsText()
        assertNotEquals(firstResponse, secondResponse, "Response should update over time")
    }
}
