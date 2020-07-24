"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01ShareRideAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write', 'update', 'superuser']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'from_place': 'string',
            'to_place': 'string',
            'date_time': 'string',
            'flexible_timings': True,
            'start_date_time': 'string',
            'end_date_time': 'string',
            'no_of_seats_available': 1,
            'assets_quantity': 1
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
