#ifndef RESPONSE_H
#define RESPONSE_H

#include "request.h"

#define MAX_RESPONSE_SIZE 104857600

typedef struct {
    int status_code;
    const char *status_text;
    const char *content_type;
    char *body;
    size_t body_length;
} http_response_t;

void generate_response(const http_request_t *request, http_response_t *response);
void send_response(int client_fd, const http_response_t *response);

#endif /* RESPONSE_H */
