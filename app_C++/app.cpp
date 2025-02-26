#include <httplib.h>
#include <string>
#include <cstdlib>  
#include <ctime>

int main() {
    srand(time(nullptr));
    httplib::Server server;

    server.Get("/", [](const httplib::Request&, httplib::Response& response) {
        int rnd = rand();
        response.set_content("Random number is: " + std::to_string(rnd), "text/plain");
    });

    server.listen("0.0.0.0", 8080);
}
