import abc
from lets_ride_auth.dtos.dtos import (
    UserAuthTokensDto
)


class PresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abc.abstractmethod
    def login_response(self, tokens_dto: UserAuthTokensDto):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_does_not_exist(self):
        pass

    # @abc.abstractmethod
    # def get_user_profile_response(self, user_profile_dto: UserDetailsDto):
    #     pass
    #
    # @abc.abstractmethod
    # def raise_exception_for_is_not_admin(self):
    #     pass
