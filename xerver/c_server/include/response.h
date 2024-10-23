#ifndef RESPONSE_H
#define RESPONSE_H

/*
 * File: response.h
 * Description: Defines structures and functions for handling HTTP responses.
 */

#define MAX_RESPONSE_SIZE 104857600

/* Prototypes */
/**
 * struct http_response_t - Represents an HTTP response.
 * @status_code: The HTTP status code (e.g., 200, 404).
 * @status_text: The text representation of the
 * status code (e.g., "OK", "Not Found").
 * @content_type: The MIME type of the response content (e.g., "text/html").
 * @body: The body of the HTTP response.
 * @body_length: The length of the body content.
 */
typedef struct http_response_t
{
	int status_code;
	const char *status_text;
	const char *content_type;
	char *body;
	size_t body_length;
} http_response_t;

/**
 * generate_response - Generates an HTTP response based on the given request.
 * @request: A pointer to the parsed HTTP request.
 * @response: A pointer to an http_response_t structure where the response
 *            will be stored.
 */
void generate_response(const http_request_t *request,
		       http_response_t *response);

/**
 * send_response - Sends an HTTP response to the client.
 * @client_fd: The file descriptor of the client socket.
 * @response: A pointer to the HTTP response to be sent.
 */
void send_response(int client_fd, const http_response_t *response);

#endif /* RESPONSE_H */
