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

    def validate_user_id(self, user_id: int) -> bool:
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise UserDoesNotExist
        return True
