#include "server.h"

int main(void) {
    int server_fd = setup_server_socket(PORT);
    while (1) {
        int *client_fd = malloc(sizeof(int));
        *client_fd = accept(server_fd, ...);
        pthread_create(&thread_id, ..., handle_client, (void *)client_fd);
    }
    return (0);
}
