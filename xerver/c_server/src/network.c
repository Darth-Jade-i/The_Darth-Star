#include "xerver.h"

/**
 * create_server_socket - Creates a server socket and binds it to a port.
 * @port: The port number to bind the server to.
 *
 * Return: The server socket file descriptor on success, -1 on failure.
 */
int create_server_socket(int port)
{
    int server_fd;
    struct sockaddr_in server_addr;

    /* Create socket */
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("socket failed");
        return (-1);
    }

    /* Set socket options */
    int opt = 1;
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)) < 0)
    {
        perror("setsockopt failed");
        close(server_fd);
        return (-1);
    }

    /* Configure server address */
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(port);

    /* Bind socket to the port */
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        perror("bind failed");
        close(server_fd);
        return (-1);
    }

    /* Start listening for connections */
    if (listen(server_fd, MAX_CONNECTIONS) < 0)
    {
        perror("listen failed");
        close(server_fd);
        return (-1);
    }

    return (server_fd);
}

/**
 * accept_client_connection - Accepts a client connection on a server socket.
 * @server_fd: The server socket file descriptor.
 * @client_addr: Pointer to store the client's address information.
 *
 * Return: The client socket file descriptor on success, -1 on failure.
 */
int accept_client_connection(int server_fd, struct sockaddr_in *client_addr)
{
    socklen_t client_addr_len = sizeof(*client_addr);
    int client_fd = accept(server_fd, (struct sockaddr *)client_addr, &client_addr_len);

    if (client_fd < 0)
    {
        perror("accept failed");
    }

    return (client_fd);
}
