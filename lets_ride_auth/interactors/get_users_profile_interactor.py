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

    def get_users_profile_wrapper(self, user_ids: List[int],
                                  presenter: PresenterInterface) -> List[UserProfileDTO]:
        try:
            return self._get_users_profile(user_ids=user_ids)
        except UserDoesNotExist:
            pass


#
# class GetUserDetailsInteractor:
#
#     def __init__(self, storage: StorageInterface):
#         self.storage = storage
#
#     def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
#         user_dtos = self.storage.get_user_details_dtos(user_ids=user_ids)
#         return user_dtos
