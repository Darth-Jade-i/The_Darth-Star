#ifndef XERVER_H
#define XERVER_H

/* C Header Files*/
#include <arpa/inet.h>
#include <ctype.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <pthread.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <unistd.h>

/* Custom Header Files */
#include "network.h"
#include "request.h"
#include "response.h"
#include "utils.h"

/* Macros/Constants */
#define PORT 8080
#define MAX_CONNECTIONS 10

/* Structs */
typedef struct {
    int client_fd;
} client_args_t;

/* Prototypes */
void *handle_client(void *arg);
void run_server(void);


#endif /* XERVER_H */
