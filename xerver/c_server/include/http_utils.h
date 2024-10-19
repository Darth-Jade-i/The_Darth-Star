#ifndef HTTP_UTILS_H
#define HTTP_UTILS_H

const char *get_file_extension(const char *file_name);
const char *get_mime_type(const char *file_ext);
char *url_decode(const char *src);
void build_http_response(const char *file_name, const char *file_ext, char *response, size_t *response_len);

#endif /* HTTP_UTILS_H */
