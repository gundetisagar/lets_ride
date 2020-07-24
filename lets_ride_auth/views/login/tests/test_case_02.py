"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "username_0",
    "password": "string"
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


class TestCase02LoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    import pytest
    @pytest.mark.django_db
    def test_case(self):
        UserFactory.reset_sequence()
        UserFactory()

        self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
