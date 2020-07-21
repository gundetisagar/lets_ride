from lets_ride_auth.presenters.presenter_implementation import PresenterImplementation
from lets_ride_auth.tests.interactors.conftest import user_auth_token_dto

def test_login_response(user_auth_token_dto):
    # Arrange
    json_presenter = PresenterImplementation()
    token_dto = user_auth_token_dto
    user_id = 1
    access_token = "VOIJxweGVtmg13Dvd4vmq7GZMz7Xfe"
    refresh_token = "Plh5j9tb2VQNhob0qeHYFEf3qLCkQt"
    expires_in = "2052-03-29 17:30:06.527606"

    # Act
    response_object = json_presenter.login_response(token_dto)

    # Act
    print(response_object)
    import json
    data = json.loads(response_object.content)
    print(data)
    assert user_id == data["user_id"]
    assert access_token == data["access_token"]
    assert refresh_token == data["refresh_token"]
    assert expires_in == data["expires_in"]
