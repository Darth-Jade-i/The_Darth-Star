#include "xerver.h"

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

    return (s);
}
