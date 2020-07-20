from lets_ride_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from lets_ride_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from lets_ride_auth.exceptions.exceptions import InvalidPassword, InvalidUsername


class LoginInteractor:
    def __init__(self, user_storage: UserStorageInterface,
                 oauth_storage: OAuthUserAuthTokensService):
        self.user_storage = user_storage
        self.oauth_storage = oauth_storage

    def login_wrapper(self, username: str, password: str, presenter: PresenterInterface):

        try:
            return self._login_response(username=username, password=password, presenter=presenter)

        except InvalidUsername:
            return presenter.raise_exception_for_invalid_username()

        except InvalidPassword:
            return presenter.raise_exception_for_invalid_password()

    def _login_response(self, username: str, password: str, presenter: PresenterInterface):
        token_dto = self.login(username=username, password=password)
        return presenter.login_response(token_dto)


    def login(self, username, password):
        self.user_storage.validate_username(username=username)

        user_id = self.user_storage.validate_password(username=username, password=password)

        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
        )

        token_dto = service.create_user_auth_tokens(
            user_id=user_id
        )
        return token_dto


