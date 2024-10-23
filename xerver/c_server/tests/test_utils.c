#include "xerver.h"

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

    return (s);
}
