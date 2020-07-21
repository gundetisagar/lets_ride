import pytest
from lets_ride_auth.dtos.dtos import UserAuthTokensDto


@pytest.fixture()
def user_auth_token_dto():
    userauthdto = UserAuthTokensDto(
        user_id=1,
        access_token="VOIJxweGVtmg13Dvd4vmq7GZMz7Xfe",
        refresh_token="Plh5j9tb2VQNhob0qeHYFEf3qLCkQt",
        expires_in="2052-03-29 17:30:06.527606"
    )
    return userauthdto
