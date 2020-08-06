# import json
# from unittest.mock import create_autospec
#
# from lets_ride_auth.presenters.presenter_implementation import \
#     PresenterImplementation
# from lets_ride_auth.tests.factories.interactor_dtos import UserProfileDtoFactory
#
#
# def test_get_users_profile_response(snapshot):
#     # Arrange
#     presenter = PresenterImplementation()
#     user_dtos = UserProfileDtoFactory.create_batch(4)
#
#     # Act
#     response_object = presenter.get_users_profile_response(user_dtos=user_dtos)
#
#     # Assert
#     print(response_object)
#     response = json.loads(response_object.content)
#     snapshot.assert_match(response, "response")
