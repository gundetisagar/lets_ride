import pytest
from lets_ride_auth.dtos.dtos import UserAuthTokensDto


@pytest.fixture()
def user_auth_token_dto():
    user_auth_dto = UserAuthTokensDto(
        user_id=1,
        access_token="12345",
        refresh_token="54321",
        expires_in=121313
    )
    return user_auth_dto
