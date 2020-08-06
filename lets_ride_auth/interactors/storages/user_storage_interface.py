import abc
from typing import List

from lets_ride_auth.dtos.dtos import UserProfileDTO


class UserStorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abc.abstractmethod
    def validate_password(self, username: str, password: str) -> int:
        pass

    @abc.abstractmethod
    def get_users_profile_dtos(self, user_ids: List[int]) -> UserProfileDTO:
        pass

    @abc.abstractmethod
    def validate_user_id(self, user_id: int) -> bool:
        pass
