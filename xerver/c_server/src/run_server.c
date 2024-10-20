#include "xerver.h"

void run_server(void) {
    int server_fd = create_server_socket(PORT);
    if (server_fd < 0) {
        fprintf(stderr, "Failed to create server socket\n");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d\n", PORT);

    while (1) {
        struct sockaddr_in client_addr;
        int client_fd = accept_client_connection(server_fd, &client_addr);
        if (client_fd < 0) {
            fprintf(stderr, "Failed to accept client connection\n");
            continue;
        }

        client_args_t *args = safe_malloc(sizeof(client_args_t));
        args->client_fd = client_fd;

        pthread_t thread_id;
        if (pthread_create(&thread_id, NULL, handle_client, args) != 0) {
            fprintf(stderr, "Failed to create thread\n");
            free(args);
            close(client_fd);
        } else {
            pthread_detach(thread_id);
        }
    }

    close(server_fd);
}
