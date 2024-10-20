# XERVER: The Darth Star.

## Include Directory

This directory contains the header files for the `Xerver` HTTP server project. These header files define the core structures, constants, and function prototypes required for handling HTTP requests, responses, network connections, and server operations. Each file in this directory serves a specific purpose in the overall functioning of the server.

## Files

### 1. `request.h`

This header file defines the structures and functions needed to handle and parse incoming HTTP requests.

#### Components:
- **Constants**:
- `MAX_URI_LENGTH`: Defines the maximum length for the URI (2048 characters).
- `MAX_HEADERS`: Specifies the maximum number of headers an HTTP request can contain.
- `MAX_HEADER_NAME_LENGTH` and `MAX_HEADER_VALUE_LENGTH`: Define the maximum lengths for header names and values, ensuring that headers are appropriately constrained.

- **Structures**:
- `http_header_t`: Represents a single HTTP header, containing a `name` and `value`.
- `http_request_t`: Represents an HTTP request, containing the HTTP method (e.g., GET, POST), the requested URI, HTTP version, an array of headers, and a header count.

- **Functions**:
- `bool parse_request(int client_fd, http_request_t *request)`: Parses an HTTP request from the client socket and populates the `http_request_t` structure. This function ensures that the request data is accurately interpreted, which is crucial for generating appropriate responses.

### 2. `response.h`

This header file defines the structures and functions used to create and send HTTP responses back to clients.

#### Components:
- **Constants**:
- `MAX_RESPONSE_SIZE`: Sets a limit for the size of the response body (100 MB). This helps prevent memory overuse and ensures efficient handling of large data payloads.

- **Structures**:
- `http_response_t`: Represents an HTTP response, including the status code (e.g., 200, 404), status text (e.g., "OK", "Not Found"), content type (e.g., "text/html"), the body of the response, and the length of the body.

- **Functions**:
- `void generate_response(const http_request_t *request, http_response_t *response)`: Creates an appropriate HTTP response based on the given request. This function interprets the request data and generates content accordingly.
- `void send_response(int client_fd, const http_response_t *response)`: Sends the generated HTTP response to the client through the provided socket file descriptor. It ensures that the client receives the correct status and data.

### 3. `network.h`

This header file defines the network operations required for setting up and managing server sockets and client connections.

#### Components:
- **Functions**:
- `int create_server_socket(int port)`: Creates a server socket and binds it to the specified port. This is the starting point for accepting client connections, and it allows the server to listen for incoming requests.
- `int accept_client_connection(int server_fd, struct sockaddr_in *client_addr)`: Accepts a client connection on the provided server socket. It returns the file descriptor of the newly accepted client connection, allowing further communication between the server and the client.

### 4. `xerver.h`

This header file acts as the central point for managing the server's operations, including handling client interactions and running the main server loop.

#### Components:
- **Constants**:
- `PORT`: Defines the default port (8080) for the server to listen on. This value can be adjusted based on deployment needs.
- `MAX_CONNECTIONS`: Sets the maximum number of simultaneous client connections that the server can handle, ensuring efficient resource management.

- **Structures**:
- `client_args_t`: Encapsulates the arguments passed to a thread handling a client. It stores the file descriptor of the client connection, allowing threads to process client requests concurrently.

- **Functions**:
- `void *handle_client(void *arg)`: Handles the communication between the server and a connected client. This function is designed to run as a separate thread for each client, enabling concurrent handling of multiple clients.
- `void run_server(void)`: Sets up the server and manages the main server loop. This function initializes the server socket, listens for incoming connections, and spawns threads to handle each client connection, ensuring the server remains responsive to new requests.

## Purpose of Each Header File

- **Modular Design**: Each header file is focused on a specific aspect of the server's functionality, which promotes modularity and code reusability. This design ensures that changes in one component do not impact others.
- **Code Clarity and Maintainability**: By clearly defining data structures and functions in separate header files, the codebase is easier to read, maintain, and extend. This separation of concerns allows for easier debugging and testing.
- **Scalability**: The design of the network and server handling functions allows for handling multiple client connections efficiently, making the server scalable and adaptable to different network loads.

## Conclusion

The header files in this `include` directory form the backbone of the `Xerver` HTTP server project, defining essential data structures and functions that enable the server to handle HTTP requests, generate responses, and manage client-server interactions. Each file is carefully structured to ensure modularity, efficiency, and ease of maintenance, making this project a robust foundation for building scalable and responsive web servers.