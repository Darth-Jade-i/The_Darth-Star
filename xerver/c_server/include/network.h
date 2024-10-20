#ifndef NETWORK_H
#define NETWORK_H

int create_server_socket(int port);
int accept_client_connection(int server_fd, struct sockaddr_in *client_addr);

#endif /* NETWORK_H */
