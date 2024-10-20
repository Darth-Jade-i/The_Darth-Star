#include "xerver.h"

int create_server_socket(int port)
{
    int server_fd;
    struct sockaddr_in server_addr;

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        perror("socket failed");
        return (-1);
    }

    int opt = 1;
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)))
    {
        perror("setsockopt failed");
        close(server_fd);
        return (-1);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(port);

    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0)
    {
        perror("bind failed");
        close(server_fd);
        return (-1);
    }

    if (listen(server_fd, MAX_CONNECTIONS) < 0)
    {
        perror("listen failed");
        close(server_fd);
        return (-1);
    }

    return server_fd;
}

int accept_client_connection(int server_fd, struct sockaddr_in *client_addr)
{
    socklen_t client_addr_len = sizeof(*client_addr);
    int client_fd = accept(server_fd, (struct sockaddr *)client_addr, &client_addr_len);
    if (client_fd < 0) {
        perror("accept failed");
    }
    return (client_fd);
}
