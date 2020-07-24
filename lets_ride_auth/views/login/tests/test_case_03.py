"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "user_1",
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
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from lets_ride_auth.dtos.dtos import UserAuthTokensDto
from unittest.mock import patch


@patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens")
class TestCase03LoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    import pytest
    @pytest.mark.django_db
    def test_case(self, patch_object):
        patch_object.return_value = UserAuthTokensDto(
            access_token='SwB855xVFhvMnI5ci59ylTstvi5CoB',
            expires_in='2052-04-01 00:33:11.590336',
            refresh_token='ztQmkfr0AKA5YxeKQOuDaOH5mtWtyp',
            user_id=1
        )
        user_obj = UserFactory(username="user_1")
        user_obj.set_password("user@1234")
        user_obj.save()
        self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
