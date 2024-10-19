#ifndef REQUEST_H
#define REQUEST_H

#include <stdbool.h>

#define MAX_URI_LENGTH 2048
#define MAX_HEADERS 50
#define MAX_HEADER_NAME_LENGTH 256
#define MAX_HEADER_VALUE_LENGTH 1024

typedef struct {
    char name[MAX_HEADER_NAME_LENGTH];
    char value[MAX_HEADER_VALUE_LENGTH];
} http_header_t;

typedef struct {
    char method[16];
    char uri[MAX_URI_LENGTH];
    char version[16];
    http_header_t headers[MAX_HEADERS];
    int header_count;
} http_request_t;

bool parse_request(int client_fd, http_request_t *request);

#endif /* REQUEST_H */
