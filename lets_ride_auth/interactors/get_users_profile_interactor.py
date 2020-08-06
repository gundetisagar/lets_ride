from typing import List

from lets_ride_auth.dtos.dtos import UserProfileDTO
from lets_ride_auth.exceptions.exceptions import UserDoesNotExist
from lets_ride_auth.interactors.presenters.presenter_interface import \
    PresenterInterface
from lets_ride_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface


class GetUsersProfileInteractor:
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    # def get_users_profile(self, user_ids: List[int],
    #                               presenter: PresenterInterface) -> List[
    #     UserProfileDTO]:
    #     user_dtos = self.get_users_profile(user_ids=user_ids)
    #     return presenter.get_users_profile_response(user_dtos)

    def get_users_profile_dtos(self, user_ids: List[int]) -> List[UserProfileDTO]:
        user_dtos = self.user_storage.get_users_profile_dtos(
            user_ids=user_ids)
        return user_dtos
