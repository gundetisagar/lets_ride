from typing import List

from lets_ride_auth.interactors.get_users_profile_interactor import \
    GetUsersProfileInteractor

class UserInterface:
    @staticmethod
    def get_users_profile_dtos(user_ids: List[int]):
        from lets_ride_auth.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        interactor = GetUsersProfileInteractor(user_storage=user_storage)
        user_profile_dtos = interactor.get_users_profile_dtos(user_ids=user_ids)
        return user_profile_dtos
