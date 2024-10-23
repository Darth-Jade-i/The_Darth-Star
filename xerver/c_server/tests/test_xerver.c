#include "xerver.h"

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
