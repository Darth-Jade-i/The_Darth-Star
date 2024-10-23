// tests/test_utils.c
#include <check.h>
#include "utils.h"
#include <string.h>

START_TEST(test_url_decode)
{
char *decoded = url_decode("hello%20world");
ck_assert_str_eq(decoded, "hello world");
free(decoded);

decoded = url_decode("test%21%40%23%24%25%5E%26%2A%28%29");
ck_assert_str_eq(decoded, "test!@#$%^&*()");
free(decoded);
}
END_TEST

START_TEST(test_get_file_extension)
{
ck_assert_str_eq(get_file_extension("test.txt"), "txt");
ck_assert_str_eq(get_file_extension("image.jpg"), "jpg");
ck_assert_str_eq(get_file_extension("noextension"), "");
ck_assert_str_eq(get_file_extension(".htaccess"), "htaccess");
}
END_TEST

START_TEST(test_get_mime_type)
{
ck_assert_str_eq(get_mime_type("html"), "text/html");
ck_assert_str_eq(get_mime_type("jpg"), "image/jpeg");
ck_assert_str_eq(get_mime_type("unknown"), "application/octet-stream");
}
END_TEST

Suite *utils_suite(void)
{
Suite *s;
TCase *tc_core;

s = suite_create("Utils");
tc_core = tcase_create("Core");

tcase_add_test(tc_core, test_url_decode);
tcase_add_test(tc_core, test_get_file_extension);
tcase_add_test(tc_core, test_get_mime_type);
suite_add_tcase(s, tc_core);

return s;
}

// tests/test_request.c
#include <check.h>
#include "request.h"
#include <string.h>
#include <unistd.h>

START_TEST(test_parse_request)
{
int pipefd[2];
pipe(pipefd);

const char *request_str = 
"GET /index.html HTTP/1.1\r\n"
"Host: example.com\r\n"
"User-Agent: Mozilla/5.0\r\n"
"\r\n";

write(pipefd[1], request_str, strlen(request_str));
close(pipefd[1]);

http_request_t request;
bool result = parse_request(pipefd[0], &request);

ck_assert(result);
ck_assert_str_eq(request.method, "GET");
ck_assert_str_eq(request.uri, "/index.html");
ck_assert_str_eq(request.version, "HTTP/1.1");
ck_assert_int_eq(request.header_count, 2);
ck_assert_str_eq(request.headers[0].name, "Host");
ck_assert_str_eq(request.headers[0].value, "example.com");

close(pipefd[0]);
}
END_TEST

Suite *request_suite(void)
{
Suite *s;
TCase *tc_core;

s = suite_create("Request");
tc_core = tcase_create("Core");

tcase_add_test(tc_core, test_parse_request);
suite_add_tcase(s, tc_core);

return s;
}

// tests/test_response.c
#include <check.h>
#include "response.h"
#include <string.h>
#include <unistd.h>

START_TEST(test_generate_response)
{
http_request_t request = {
.method = "GET",
.uri = "/index.html",
.version = "HTTP/1.1"
};

http_response_t response = {0};
generate_response(&request, &response);

ck_assert_int_eq(response.status_code, 404); // Assuming file doesn't exist
ck_assert_str_eq(response.status_text, "Not Found");
ck_assert_str_eq(response.content_type, "text/plain");
ck_assert_str_eq(response.body, "404 Not Found");

free(response.body);
}
END_TEST

Suite *response_suite(void)
{
Suite *s;
TCase *tc_core;

s = suite_create("Response");
tc_core = tcase_create("Core");

tcase_add_test(tc_core, test_generate_response);
suite_add_tcase(s, tc_core);

return s;
}

// tests/test_network.c
#include <check.h>
#include "network.h"
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

START_TEST(test_create_server_socket)
{
int server_fd = create_server_socket(8080);
ck_assert_int_ge(server_fd, 0);
close(server_fd);
}
END_TEST

Suite *network_suite(void)
{
Suite *s;
TCase *tc_core;

s = suite_create("Network");
tc_core = tcase_create("Core");

tcase_add_test(tc_core, test_create_server_socket);
suite_add_tcase(s, tc_core);

return s;
}

// tests/test_http_server.c
#include <check.h>

extern Suite *utils_suite(void);
extern Suite *request_suite(void);
extern Suite *response_suite(void);
extern Suite *network_suite(void);

int main(void)
{
int number_failed;
SRunner *sr;

sr = srunner_create(utils_suite());
srunner_add_suite(sr, request_suite());
srunner_add_suite(sr, response_suite());
srunner_add_suite(sr, network_suite());

srunner_run_all(sr, CK_NORMAL);
number_failed = srunner_ntests_failed(sr);
srunner_free(sr);
return (number_failed == 0) ? 0 : 1;
}
