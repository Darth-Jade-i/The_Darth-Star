#ifndef XERVER_H
#define XERVER_H

/*
 * File: xerver.h
 * Description: Header file for the Xerver HTTP server. Includes necessary
 *              libraries, constants, data structures, and function prototypes
 *              for running the server and handling client connections.
 */

/* C Header Files */
#include <arpa/inet.h>
#include <check.h>
#include <ctype.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <pthread.h>
#include <stdbool.h>
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

/**
 * struct client_args_t - Arguments passed to a thread handling a client.
 * @client_fd: The file descriptor for the client connection.
 */
typedef struct client_args_t
{
	int client_fd;
} client_args_t;

/**
 * handle_client - Handles the communication with a connected client.
 * @arg: A pointer to a client_args_t structure
 * containing the client file descriptor.
 * Return: A pointer to the return value, NULL in this case.
 */
void *handle_client(void *arg);

/**
 * run_server - Initializes and runs the Xerver HTTP server.
 *
 * Return: void.
 */
void run_server(void);

#endif /* XERVER_H */
