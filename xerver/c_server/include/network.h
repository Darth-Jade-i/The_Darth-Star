#ifndef NETWORK_H
#define NETWORK_H

/*
 * File: network.h
 * Description: Contains function prototypes for creating a server socket
 * and accepting client connections.
 */

/**
 * create_server_socket - Creates a server socket and
 * binds it to the specified port.
 * @port: The port number to bind the server socket to.
 *
 * Return: The file descriptor of the created server socket on success,
 * or -1 on failure.
 */
int create_server_socket(int port);

/**
 * accept_client_connection - Accepts a new client connection
 * on the server socket.
 * @server_fd: The file descriptor of the server socket.
 * @client_addr: A pointer to a sockaddr_in structure
 * to store the client's address.
 *
 * Return: The file descriptor for the accepted client connection on success,
 * or -1 on failure.
 */
int accept_client_connection(int server_fd, struct sockaddr_in *client_addr);

#endif /* NETWORK_H */
