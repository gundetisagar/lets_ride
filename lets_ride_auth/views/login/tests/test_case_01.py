"""
# TODO: Login API test case with invalid username and raises error and gives error message
"""
import self as self
from django_swagger_utils.utils.test import CustomAPITestCase

from lets_ride_auth.models import User
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "user",
    "password": "user@1234"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}

from lets_ride_auth.tests.factories.models import UserFactory


class TestCase01LoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    user_obj = UserFactory(username="user")
    user_obj.set_password("user123")
    user_obj.save()

    def test_case(self):
        response = self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
