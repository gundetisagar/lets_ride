import abc
from typing import List

from django.http import HttpResponse

from lets_ride_auth.dtos.dtos import (
    UserAuthTokensDto, UserProfileDTO
)


class PresenterInterface(abc.ABC):
    @abc.abstractmethod
    def raise_exception_for_invalid_username(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_password(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def login_response(self, tokens_dto: UserAuthTokensDto) -> HttpResponse:
        pass
    #
    # @abc.abstractmethod
    # def raise_exception_for_user_does_not_exist(self):
    #     pass

    # @abc.abstractmethod
    # def get_users_profile_response(self, user_dtos: List[UserProfileDTO]):
    #     pass
