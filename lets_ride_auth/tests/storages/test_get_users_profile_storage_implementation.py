from unittest.mock import create_autospec

import pytest

from lets_ride_auth.storages.user_storage_implementation import \
    UserStorageImplementation
from lets_ride_auth.tests.factories.interactor_dtos import UserProfileDtoFactory
from lets_ride_auth.tests.factories.models import UserFactory

@pytest.mark.django_db
def test_get_user_profile():
    # Arragne
    user_ids = [1, 2, 3]
    user_storage = create_autospec(UserStorageImplementation)
    UserFactory.create_batch(3)
    expected_users_profile_dto = UserProfileDtoFactory.create_batch(size=3)
    user_storage.get_users_profile_dtos.return_value = expected_users_profile_dto

    # Act
    users_profile_dto = user_storage.get_users_profile_dtos(user_ids=user_ids)

    # Assert
    assert expected_users_profile_dto == users_profile_dto
