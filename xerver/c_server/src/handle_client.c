#include "xerver.h"

void *handle_client(void *arg) {
    client_args_t *args = (client_args_t *)arg;
    int client_fd = args->client_fd;
    free(args);

    http_request_t request;
    http_response_t response = {0};

    if (parse_request(client_fd, &request)) {
        generate_response(&request, &response);
        send_response(client_fd, &response);
    } else {
        fprintf(stderr, "Failed to parse request\n");
    }

    free(response.body);
    close(client_fd);
    return NULL;
}
