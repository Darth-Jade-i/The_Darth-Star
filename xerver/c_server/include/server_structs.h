#ifndef XERVER_STRUCTS_H
#define XERVER_STRUCTS_H

#include <netinet/in.h>

/* Structure for client thread data */
typedef struct
{
    int client_fd;
    struct sockaddr_in client_addr;
} ClientData;

/* Structure for server configuration */
typedef struct {
    int port;
    int max_clients;
    int server_fd;
    struct sockaddr_in server_addr;
} ServerConfig;

#endif /* SERVER_STRUCTS_H */
