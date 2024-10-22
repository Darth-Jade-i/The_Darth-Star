#include "xerver.h"

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

    return (s);
}
