
from unittest.mock import create_autospec, patch, Mock
import pytest
from lets_ride_auth.interactors.login_interactor import LoginInteractor
from lets_ride_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from lets_ride_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage
from lets_ride_auth.exceptions.exceptions import InvalidUsername, InvalidPassword


def test_user_login_with_invalid_username():
    # Arrange
    username = "sagar"
    password = "1234"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuthUserAuthTokensService)

    user_storage.validate_username.side_effect = InvalidUsername
    mock_object = Mock()
    presenter.raise_exception_for_invalid_username.return_value = mock_object
    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth_storage=oauth_storage
    )

    response = interactor.login_wrapper(
        username=username,
        password=password,
        presenter=presenter
        )

    # Assert
    assert response == mock_object
    user_storage.validate_username.assert_called_once_with(username=username)
    presenter.raise_exception_for_invalid_username.assert_called_once()



def test_user_login_with_invalid_password():
    # Arrange
    username = "sagar"
    password = "1234"
    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuthUserAuthTokensService)

    user_storage.validate_username.return_value = True
    user_storage.validate_password.side_effect = InvalidPassword
    mock_object = Mock()
    presenter.raise_exception_for_invalid_password.return_value = mock_object
    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth_storage=oauth_storage
    )

    # Act
    response = interactor.login_wrapper(username=username, password=password, presenter=presenter)

    # Assert
    user_storage.validate_password.assert_called_once_with(username=username, password=password)
    presenter.raise_exception_for_invalid_password.assert_called_once()
    assert response == mock_object

from lets_ride_auth.tests.interactors.dtos import user_auth_token_dto


@patch("common.oauth_user_auth_tokens_service.OAuthUserAuthTokensService.create_user_auth_tokens")
def test_user_login_interactor(token_mock, user_auth_token_dto):
    print("*"*10, user_auth_token_dto)
    # Arrange
    username = "sagar"
    password = "123"
    user_id = 1
    expected_dict = {
        "user_id": 1,
        "access_token": "123456",
        "refresh_token": "54321",
        "expires_in": 121313
    }

    user_storage = create_autospec(UserStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuthUserAuthTokensService)
    oauth2_storage = create_autospec(OAuth2SQLStorage)

    user_storage.validate_username.return_value = True
    user_storage.validate_password.return_value = user_id
    presenter.login_response.return_value = expected_dict
    token_mock.return_value = user_auth_token_dto

    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth_storage=oauth2_storage
    )
    # Act
    service = interactor.login_wrapper(username=username, password=password, presenter=presenter)

    # Assert
    assert service == expected_dict
    oauth_storage.create_user_auth_tokens.assert_called_once_with(
        user_id=user_id
    )
