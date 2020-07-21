from lets_ride_auth.presenters.presenter_implementation import PresenterImplementation
from lets_ride_auth.constants.exception_messages import INVALID_PASSWORD


def test_raise_exception_for_invalid_username():
    # Arrange
    json_presenter = PresenterImplementation()
    expected_response = INVALID_PASSWORD[0]
    expected_res_status = INVALID_PASSWORD[1]

    # Act
    response_object = json_presenter.raise_exception_for_invalid_password()

    # Act
    import json
    response = json.loads(response_object.content)
    assert response['http_status_code'] == 400
    assert response['res_status'] == expected_res_status
    assert response['response'] == expected_response
