"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "from_place": "hyd",
    "to_place": "kurnool",
    "datetime": null,
    "flexible_timings": true,
    "start_datetime": "2020-05-27 05:06:27",
    "end_datetime": "2020-06-30 05:06:29",
    "no_of_seats": 1,
    "luggage_quantity": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/",
                                 "flow": "password",
                                 "scopes": ["read", "write", "update"],
                                 "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01RideRequestAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01RideRequestAPITestCase, self).setupUser(
            username=username, password=password
        )

    def test_case(self):
        self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
