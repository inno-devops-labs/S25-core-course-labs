#include <httplib.h>
#include <string>
#include <cstdlib>  
#include <ctime>
#include <fstream>
#include <iostream>

int read_visits() {
    std::ifstream file("visits.txt");
    int visits = 0;
    if (file.is_open()) {
        file >> visits;
        file.close();
    }
    return visits;
}

void write_visits(int visits) {
    std::ofstream file("visits.txt");
    if (file.is_open()) {
        file << visits;
        file.close();
    }
}

int main() {
    srand(time(nullptr));
    httplib::Server server;

    server.Get("/", [](const httplib::Request&, httplib::Response& response) {
        int rnd = rand();
        response.set_content("Random number is: " + std::to_string(rnd), "text/plain");
    });

    server.Get("/visits", [](const httplib::Request&, httplib::Response& response) {
        int visits = read_visits();
        visits++;
        write_visits(visits);
        response.set_content("Total visits: " + std::to_string(visits), "text/plain");
    });

    server.listen("0.0.0.0", 8080);
}
