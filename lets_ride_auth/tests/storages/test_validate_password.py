import pytest
from lets_ride_auth.storages.user_storage_implementation import UserStorageImplementation
from lets_ride_auth.exceptions.exceptions import InvalidPassword


@pytest.mark.django_db
def test_validate_password_with_invalid_password_and_raises_exception():
    # Arrange
    username = "username"
    invalid_password = "invalid_password"
    user_storage = UserStorageImplementation()
    from lets_ride_auth.tests.factories.models import UserFactory
    UserFactory(username="username", password="password")

    # Act
    with pytest.raises(InvalidPassword):
        user_storage.validate_password(username=username, password="password")




@pytest.mark.django_db
def test_validate_password_with_valid_password_returns_user_id():
    # Arrange
    username = "username"
    password = "user@1234"
    user_id = 1
    user_storage = UserStorageImplementation()
    from lets_ride_auth.tests.factories.models import UserFactory
    user_object = UserFactory(username=username)
    user_object.set_password(password)
    user_object.save()

    # Act
    response = user_storage.validate_password(username=username, password=password)

    # Assert
    assert response == user_id
