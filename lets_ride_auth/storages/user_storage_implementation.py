from typing import List

from lets_ride_auth.dtos.dtos import UserProfileDTO
from lets_ride_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from lets_ride_auth.exceptions.exceptions import (
    InvalidUsername,
    InvalidPassword,
    UserDoesNotExist
)
from lets_ride_auth.models.user import User


class UserStorageImplementation(UserStorageInterface):

    def validate_username(self, username: str) -> bool:
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername
        return True

    def validate_password(self, username: str, password: str) -> int:
        user_obj = User.objects.get(username=username)
        if not user_obj.check_password(password):
            raise InvalidPassword
        user_id = user_obj.id
        return user_id

    def get_users_profile_dtos(self, user_ids: List[int]) -> List[
        UserProfileDTO]:

        users_profile_dict = User.objects.filter(id__in=user_ids).values(
            "id", "username",
            "name",
            "mobile_number")
        users_profile_dtos_list = []
        for user_profile in users_profile_dict:
            user_dto = self._convert_user_dict_to_dto(user_profile)
            users_profile_dtos_list.append(user_dto)
        return users_profile_dtos_list

    def _convert_user_dict_to_dto(self, user_profile: dict):
        user_dto = UserProfileDTO(
            user_id=user_profile["user_id"],
            username=user_profile["username"],
            name=user_profile["name"],
            mobile_number=user_profile["mobile_number"]
        )
        return user_dto

    def validate_user_id(self, user_id: int) -> bool:
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise UserDoesNotExist
        return True
