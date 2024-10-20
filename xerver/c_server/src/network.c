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
	server_fd = socket(AF_INET, SOCK_STREAM, 0);

	if (server_fd < 0)
	{
		perror("socket failed");
		return (-1);
	}

	/* Set socket options */
	if (set_socket_options(server_fd) < 0)
	{
		close(server_fd);
		return (-1);
	}

	/* Configure server address */
	configure_server_address(&server_addr, port);

	/* Bind socket to the port */
	if (bind_socket(server_fd, &server_addr) < 0)
	{
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
 * set_socket_options - Sets options for the server socket.
 * @server_fd: The server socket file descriptor.
 *
 * Return: 0 on success, -1 on failure.
 */
int set_socket_options(int server_fd)
{
	int opt = 1;

	if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt,
		       sizeof(opt)) < 0)
	{
		perror("setsockopt failed");
		return (-1);
	}
	return (0);
}

/**
 * configure_server_address - Configures the server address struct.
 * @server_addr: Pointer to the server address structure.
 * @port: The port number to bind the server to.
 */
void configure_server_address(struct sockaddr_in *server_addr, int port)
{
	server_addr->sin_family = AF_INET;
	server_addr->sin_addr.s_addr = INADDR_ANY;
	server_addr->sin_port = htons(port);
}

/**
 * bind_socket - Binds the server socket to an address.
 * @server_fd: The server socket file descriptor.
 * @server_addr: Pointer to the server address structure.
 *
 * Return: 0 on success, -1 on failure.
 */
int bind_socket(int server_fd, struct sockaddr_in *server_addr)
{
	if (bind(server_fd, (struct sockaddr *)server_addr,
		 sizeof(*server_addr)) < 0)
	{
		perror("bind failed");
		return (-1);
	}
	return (0);
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
	int client_fd = accept(server_fd, (struct sockaddr *)client_addr,
			       &client_addr_len);

	if (client_fd < 0)
	{
		perror("accept failed");
	}

	return (client_fd);
}
