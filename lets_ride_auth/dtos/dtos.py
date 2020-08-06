from dataclasses import dataclass


@dataclass()
class UserAuthTokensDto:
    user_id: int
    access_token: str
    refresh_token: str
    expires_in: int


@dataclass()
class UserProfileDTO:
    user_id: int
    username: str
    name: str
    mobile_number: int
