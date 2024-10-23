#include "xerver.h"

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

    return (s);
}
