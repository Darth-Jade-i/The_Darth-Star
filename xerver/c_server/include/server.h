#ifndef XERVER_H
#define XERVER_H

/* C Header files */
#include <arpa/inet.h>
#include <ctype.h>
#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <pthread.h>
#include <regex.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

/* Xerver Header Files */
#include "xerver_structs.h"
#include "http_utils.h"
#include "file_utils.h"
#include "network_utils.h"
#include "handle_client.h"

/*MACROS*/
#define PORT 8080
#define BUFFER_SIZE 104857600

#endif /* XERVER_H */
