#include "xerver.h"

int main(void)
{
    /* Create and setup server socket */
    int server_fd = setup_server_socket(PORT);
    printf("Server listening on port %d\n", PORT);

    while (1)
    {
        struct sockaddr_in client_addr;
        socklen_t client_addr_len = sizeof(client_addr);
        int *client_fd = malloc(sizeof(int));

        /* Accept client connections */
        if ((*client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_addr_len)) < 0) {
            perror("accept failed");
            free(client_fd);
            continue;
        }

        // Create a new thread to handle the client request
        pthread_t thread_id;
        ClientData *client_data = malloc(sizeof(ClientData));
        client_data->client_fd = *client_fd;
        client_data->client_addr = client_addr;
        pthread_create(&thread_id, NULL, handle_client, (void *)client_data);
        pthread_detach(thread_id);
    }

    close(server_fd);
    return 0;
}
