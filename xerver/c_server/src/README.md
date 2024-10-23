# XERVER - Source Files

## Overview

This project implements a simple multi-threaded HTTP server in C. The server is designed to handle basic HTTP requests and responses, allowing clients to retrieve files from the server's filesystem. The project is structured into several source files, each responsible for a specific functionality, promoting modularity and maintainability.

## Source Files

### 1. `xerver.c`

This file serves as the entry point for the server application. It contains the `main` function, which initializes and starts the server.

**Key Functions:**
- **`int main(void)`**: Calls the `run_server` function to start listening for incoming connections on the defined port.

### 2. `run_server.c`

This file contains the implementation of the `run_server` function, which manages the main server loop. It handles incoming client connections and spawns threads to handle each client.

**Key Functions:**
- **`void run_server(void)`**:
- Creates a server socket using `create_server_socket`.
- Enters an infinite loop to accept client connections.
- For each accepted connection, allocates memory for `client_args_t`, creates a new thread using `pthread_create` to handle the client via `handle_client`.

### 3. `handle_client.c`

This file contains the logic for processing client requests. It retrieves the HTTP request from the client, generates an appropriate response, and sends it back.

**Key Functions:**
- **`void *handle_client(void *args)`**:
- Extracts the client file descriptor from `args`.
- Parses the HTTP request using `parse_request`.
- Generates the HTTP response using `generate_response`.
- Sends the response back to the client using `send_response`.
- Frees any allocated resources and closes the client connection.

### 4. `network.c`

This file contains functions related to network operations, including creating sockets and accepting client connections.

**Key Functions:**
- **`int create_server_socket(int port)`**:
- Creates a TCP socket and binds it to the specified port.
- Sets socket options and listens for incoming connections.
- **`int accept_client_connection(int server_fd, struct sockaddr_in *client_addr)`**: 
- Accepts a client connection and fills the provided `client_addr` structure with the client's address information.

### 5. `request.c`

This file is responsible for parsing HTTP requests received from clients. It extracts the request line and headers.

**Key Functions:**
- **`bool parse_request(int client_fd, http_request_t *request)`**:
- Reads data from the client socket and extracts the request line and headers.
- Calls `parse_request_line` and `parse_header` to handle different parts of the request.

### 6. `response.c`

This file handles the generation and sending of HTTP responses. It constructs responses based on the client's requests and sends them back.

**Key Functions:**
- **`void generate_response(const http_request_t *request, http_response_t *response)`**: 
- Processes the request and sets the appropriate HTTP status and content based on the requested resource.
- Handles various response scenarios, including success, file not found, and method not allowed.
- **`void send_response(int client_fd, const http_response_t *response)`**:
- Constructs the HTTP response headers and body, sending them over the client socket.

### 7. `utils.c`

This file contains utility functions that assist with common tasks throughout the server code, such as memory allocation and string manipulation.

**Key Functions:**
- **`char *url_decode(const char *src)`**:
- Decodes URL-encoded strings, converting `%`-encoded characters back to their original form.
- **`void *safe_malloc(size_t size)`**:
- Allocates memory and checks for allocation failures, exiting the program if the allocation fails.
- **`const char *get_file_extension(const char *file_name)`**:
- Retrieves the file extension from a given filename.
- **`const char *get_mime_type(const char *file_ext)`**:
- Maps file extensions to their corresponding MIME types.

## Conclusion

This project showcases the implementation of a basic multi-threaded HTTP server in C. Each source file is designed with specific responsibilities in mind, promoting code reusability and clarity. By understanding the structure and functionality of each component, developers can easily modify and expand the server's capabilities.