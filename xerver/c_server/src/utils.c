#include "xerver.h"

char *url_decode(const char *src)
{
    size_t src_len = strlen(src);
    char *decoded = safe_malloc(src_len + 1);
    size_t decoded_len = 0;

    for (size_t i = 0; i < src_len; i++)
    {
        if (src[i] == '%' && i + 2 < src_len)
	{
            int hex_val;
            sscanf(src + i + 1, "%2x", &hex_val);
            decoded[decoded_len++] = hex_val;
            i += 2;
        }
	else if (src[i] == '+')
	{
            decoded[decoded_len++] = ' ';
        }
	else
	{
            decoded[decoded_len++] = src[i];
        }
    }

    decoded[decoded_len] = '\0';
    return (decoded);
}

const char *get_file_extension(const char *file_name)
{
    const char *dot = strrchr(file_name, '.');
    if (!dot || dot == file_name)
    {
        return "";
    }
    return (dot + 1);
}

const char *get_mime_type(const char *file_ext)
{
    if (strcasecmp(file_ext, "html") == 0 || strcasecmp(file_ext, "htm") == 0)
    {
        return "text/html";
    }
    else if (strcasecmp(file_ext, "txt") == 0)
    {
        return "text/plain";
    }
    else if (strcasecmp(file_ext, "css") == 0)
    {
        return "text/css";
    }
    else if (strcasecmp(file_ext, "js") == 0)
    {
        return "application/javascript";
    }
    else if (strcasecmp(file_ext, "jpg") == 0 || strcasecmp(file_ext, "jpeg") == 0)
    {
        return "image/jpeg";
    }
    else if (strcasecmp(file_ext, "png") == 0)
    {
        return "image/png";
    }
    else if (strcasecmp(file_ext, "gif") == 0)
    {
        return "image/gif";
    } else
    {
        return "application/octet-stream";
    }
}

void *safe_malloc(size_t size)
{
    void *ptr = malloc(size);
    if (ptr == NULL)
    {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    return (ptr);
}
