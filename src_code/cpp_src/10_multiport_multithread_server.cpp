#include <iostream>
#include <thread>
#include <httplib.h>

void handle_post(const httplib::Request& req, httplib::Response& res) {
    // Get user input from the command line
    std::string post_data;
    std::cout << "Enter post data: ";
    std::getline(std::cin, post_data);

    // Respond with user input
    res.set_content(post_data, "text/plain");
}

void run_server(const char* host, int port) {
    // Create HTTP server
    httplib::Server svr;

    // Define endpoint for handling POST requests
    svr.Post("/update_post", handle_post);

    // Run the server on the specified host and port
    svr.listen(host, port);
}

int main() {
    // List of ports to listen on
    std::vector<int> ports = {8080, 8081}; // Add more ports as needed

    // Start a separate thread for each port
    std::vector<std::thread> threads;
    for (int port : ports) {
        threads.emplace_back(run_server, "localhost", port);
    }

    // Join all threads
    for (auto& t : threads) {
        t.join();
    }

    return 0;
}
