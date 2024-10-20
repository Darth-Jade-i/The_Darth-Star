#include "xerver.h"

#define BUFFER_SIZE 4096

/**
 * parse_request_line - Parses the request line of an HTTP request.
 * @line: The request line as a string.
 * @request: Pointer to the http_request_t structure to fill.
 *
 * Return: true if parsing is successful, false otherwise.
 */
static bool parse_request_line(char *line, http_request_t *request)
{
	char *method = strtok(line, " ");
	char *uri = strtok(NULL, " ");
	char *version = strtok(NULL, "\r\n");

	if (!method || !uri || !version)
	{
		return (false);
	}

	strncpy(request->method, method, sizeof(request->method) - 1);

	char *decoded_uri = url_decode(uri);

	strncpy(request->uri, decoded_uri, sizeof(request->uri) - 1);
	free(decoded_uri);
	strncpy(request->version, version, sizeof(request->version) - 1);
	return (true);
}

/**
 * parse_header - Parses a header line of an HTTP request.
 * @line: The header line as a string.
 * @request: Pointer to the http_request_t structure to fill.
 *
 * Return: true if parsing is successful, false otherwise.
 */
static bool parse_header(char *line, http_request_t *request)
{
	char *name = strtok(line, ":");
	char *value = strtok(NULL, "\r\n");

	if (!name || !value)
	{
		return (false);
	}

/* Remove leading whitespace from value */
	while (*value == ' ')
	{
		value++;
	}
	if (request->header_count < MAX_HEADERS)
	{
		strncpy(request->headers[request->header_count].name, name,
			MAX_HEADER_NAME_LENGTH - 1);
		strncpy(request->headers[request->header_count].value, value,
			MAX_HEADER_VALUE_LENGTH - 1);
		request->header_count++;
	}

	return (true);
}

/**
 * parse_request - Reads and parses an HTTP request from a client socket.
 * @client_fd: The file descriptor of the client socket.
 * @request: Pointer to the http_request_t structure to fill.
 *
 * Return: true if the request is complete and valid, false otherwise.
 * TO DO: More than 40 lines in function
 */
bool parse_request(int client_fd, http_request_t *request)
{
	char buffer[BUFFER_SIZE];
	ssize_t bytes_read;
	size_t total_bytes = 0;
	bool request_line_parsed = false;

	memset(request, 0, sizeof(*request));

	while ((bytes_read = read(client_fd, buffer + total_bytes,
				  sizeof(buffer) - total_bytes - 1)) > 0)
	{
		total_bytes += bytes_read;
		buffer[total_bytes] = '\0';

		char *line_start = buffer;
		char *line_end;

		while ((line_end = strstr(line_start, "\r\n")) != NULL)
		{
			*line_end = '\0';

			if (!request_line_parsed)
			{
				if (!parse_request_line(line_start, request))
				{
					return (false);
				}

				request_line_parsed = true;
			}
			else if (line_start == line_end)
			{/* Empty line, end of headers */
				return (true);
			}
			else
			{
				if (!parse_header(line_start, request))
				{
					return (false);
				}
			}

			line_start = line_end + 2;
		}
/* Move remaining partial line to the beginning of the buffer */
		size_t remaining = total_bytes - (line_start - buffer);

		memmove(buffer, line_start, remaining);
		total_bytes = remaining;
	}
	return (false); /* Incomplete request */
}
