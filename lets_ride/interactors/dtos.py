import dataclasses
from datetime import datetime
from typing import List

from lets_ride.dtos.dtos import RideRequestDTO
from lets_ride_auth.dtos.dtos import UserProfileDTO


@dataclasses.dataclass
class MyRideRequestsQueryDTO:
    user_id: int
    offset: int
    limit: int
    sort_field: str
    sort_by_field: str
    filter: str


@dataclasses.dataclass
class MyRideRequestDTO:
    user_id: int
    from_place: str
    to_place: str
    date_time: datetime
    flexible_timings: bool
    start_date_time: datetime
    end_date_time: datetime
    no_of_seats: int
    luggage_quantity: int
    accepted_person: int
    status: str


@dataclasses.dataclass
class MyRideRequestWithUserProfileDTO:
    ride_request_dtos: List[MyRideRequestDTO]
    user_profile_dtos: List[UserProfileDTO]
