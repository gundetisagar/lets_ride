import pytest
from lets_ride_auth.storages.user_storage_implementation import UserStorageImplementation
from lets_ride_auth.exceptions.exceptions import InvalidUsername


@pytest.mark.django_db
def test_validate_username_with_invalid_username_and_raises_exception():
    # Arrange
    username = "username"
    user_storage = UserStorageImplementation()

    # Act
    with pytest.raises(InvalidUsername):
        user_storage.validate_username(username=username)

@pytest.mark.django_db
def test_validate_username_with_valid_username_returns_true():
    # Arrange
    invalid_username = "invalid_username"
    password = "user@1234"
    user_storage = UserStorageImplementation()
    return_value = True

    from lets_ride_auth.tests.factories.models import UserFactory
    user_object = UserFactory(username=invalid_username)
    user_object.set_password(password)
    user_object.save()

    # Act
    response = user_storage.validate_username(username=invalid_username)

    # Assert
    assert response == return_value
