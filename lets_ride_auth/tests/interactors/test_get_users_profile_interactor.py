from unittest.mock import create_autospec

from lets_ride_auth.interactors.storages.user_storage_interface import \
    UserStorageInterface
from lets_ride_auth.tests.factories.interactor_dtos import UserProfileDtoFactory


class TestGetUsersProfile:

    def test_get_users_profile_dtos(self):
        # Arrange
        user_ids = [1, 2, 3]
        user_storage = create_autospec(UserStorageInterface)
        users_profile_dtos = UserProfileDtoFactory.create_batch(3)
        user_storage.get_users_profile_dtos.return_value = users_profile_dtos

        # Act
        response_dtos = user_storage.get_users_profile_dtos(user_ids=user_ids)

        # Assert
        assert users_profile_dtos == response_dtos
