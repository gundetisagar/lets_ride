
import pytest
from lets_ride_auth.presenters.presenter_implementation import PresenterImplementation
from lets_ride_auth.constants.exception_messages import INVALID_USERNAME

def test_raise_exception_for_invalid_username():
    # Arrange
    json_presenter = PresenterImplementation()
    exception_message = INVALID_USERNAME[0]
    exception_res_status = INVALID_USERNAME[1]

    # Act
    response_object = json_presenter.raise_exception_for_invalid_username()

    # Act
    import json
    response = json.loads(response_object.content)
    assert response['http_status_code'] == 400
    assert response['res_status'] == response_status_code
    assert response['response'] == expected_response
