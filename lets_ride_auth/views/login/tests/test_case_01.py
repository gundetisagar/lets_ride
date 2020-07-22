"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "string",
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


class TestCase01LoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    import pytest
    @pytest.mark.django_db
    def test_case(self):
        UserFactory()
        print("*"*100)
        from lets_ride_auth.models import User
        print(User.objects.all().values())
        response = self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        print(response)
        import json
        response_content = json.dumps(response.content)
        print(response_data)

        # response_content = json.loads(response.content)
        #
        # comment_id = response_content['comment_id']
        #
        # comment = Comment.objects.get(id=comment_id)
        #
        # self.assert_match_snapshot(
        #     name='user_id',
        #     value=comment.user_id
        # )
        #
        # self.assert_match_snapshot(
        #     name='post_id',
        #     value=comment.post.id
        # )
        # self.assert_match_snapshot(
        #     name='comment_text',
        #     value=comment.comment_text
        # )
