
#ifndef UTILS_H
#define UTILS_H

#include <stddef.h>

char *url_decode(const char *src);
const char *get_file_extension(const char *file_name);
const char *get_mime_type(const char *file_ext);
void *safe_malloc(size_t size);

#endif /* UTILS_H */
