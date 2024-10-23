#ifndef REQUEST_H
#define REQUEST_H

/*
 * File: request.h
 * Description: Contains the definitions and structures for handling
 * HTTP requests.
 */

#define MAX_URI_LENGTH 2048
#define MAX_HEADERS 50
#define MAX_HEADER_NAME_LENGTH 256
#define MAX_HEADER_VALUE_LENGTH 1024

/**
 * struct http_header_t - Represents a single HTTP header.
 * @name: The name of the HTTP header.
 * @value: The value of the HTTP header.
 */
typedef struct http_header_t
{
	char name[MAX_HEADER_NAME_LENGTH];
	char value[MAX_HEADER_VALUE_LENGTH];
} http_header_t;

/**
 * struct http_request_t - Represents an HTTP request.
 * @method: The HTTP method (e.g., GET, POST).
 * @uri: The requested URI.
 * @version: The HTTP version (e.g., HTTP/1.1).
 * @headers: An array of HTTP headers.
 * @header_count: The number of headers in the request.
 */
typedef struct http_request_t
{
	char method[16];
	char uri[MAX_URI_LENGTH];
	char version[16];
	http_header_t headers[MAX_HEADERS];
	int header_count;
} http_request_t;

/*
 * parse_request - Parses an HTTP request from a client.
 * @client_fd: The file descriptor of the client socket.
 * @request: A pointer to an http_request_t structure where the request data
 * will be stored.
 *
 * Return: true if the request is parsed successfully, false otherwise.
 */
bool parse_request(int client_fd, http_request_t *request);

#endif /* REQUEST_H */
