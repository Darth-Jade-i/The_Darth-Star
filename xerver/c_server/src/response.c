#include "xerver.h"

static void set_response_status(http_response_t *response, int status_code, const char *status_text)
{
    response->status_code = status_code;
    response->status_text = status_text;
}

static void set_response_content(http_response_t *response, const char *content_type, const char *body, size_t body_length)
{
    response->content_type = content_type;
    response->body = safe_malloc(body_length);
    memcpy(response->body, body, body_length);
    response->body_length = body_length;
}

void generate_response(const http_request_t *request, http_response_t *response)
{
    if (strcmp(request->method, "GET") != 0)
    {
        set_response_status(response, 405, "Method Not Allowed");
        set_response_content(response, "text/plain", "405 Method Not Allowed", 22);
        return;
    }

    const char *file_name = request->uri + 1; // Skip leading '/'
    if (strlen(file_name) == 0)
    {
        file_name = "index.html";
    }

    int file_fd = open(file_name, O_RDONLY);
    if (file_fd == -1)
    {
        set_response_status(response, 404, "Not Found");
        set_response_content(response, "text/plain", "404 Not Found", 13);
        return;
    }

    struct stat file_stat;
    fstat(file_fd, &file_stat);
    off_t file_size = file_stat.st_size;

    if (file_size > MAX_RESPONSE_SIZE)
    {
        close(file_fd);
        set_response_status(response, 413, "Payload Too Large");
        set_response_content(response, "text/plain", "413 Payload Too Large", 22);
        return;
    }

    char *file_content = safe_malloc(file_size);
    ssize_t bytes_read = read(file_fd, file_content, file_size);
    close(file_fd);

    if (bytes_read != file_size)
    {
        free(file_content);
        set_response_status(response, 500, "Internal Server Error");
        set_response_content(response, "text/plain", "500 Internal Server Error", 25);
        return;
    }

    const char *file_ext = get_file_extension(file_name);
    const char *mime_type = get_mime_type(file_ext);

    set_response_status(response, 200, "OK");
    set_response_content(response, mime_type, file_content, file_size);
    free(file_content);
}

void send_response(int client_fd, const http_response_t *response) {
    char header[1024];
    int header_len = snprintf(header, sizeof(header),
                              "HTTP/1.1 %d %s\r\n"
                              "Content-Type: %s\r\n"
                              "Content-Length: %zu\r\n"
                              "\r\n",
                              response->status_code, response->status_text,
                              response->content_type, response->body_length);

    if (write(client_fd, header, header_len) != header_len) {
        fprintf(stderr, "Failed to send response header\n");
        return;
    }

    size_t total_sent = 0;
    while (total_sent < response->body_length) {
        ssize_t sent = write(client_fd, response->body + total_sent, response->body_length - total_sent);
        if (sent < 0) {
            fprintf(stderr, "Failed to send response body\n");
            return;
        }
        total_sent += sent;
    }
}
