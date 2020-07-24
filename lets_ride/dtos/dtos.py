import dataclasses
from typing import Optional

import datetime


@dataclasses.dataclass
class RideRequestDTO:
    user_id: int
    from_place: str
    to_place: str
    date_time: datetime
    flexible_timings: bool
    start_date_time: datetime
    end_date_time: datetime
    no_of_seats: int
    luggage_quantity: int


@dataclasses.dataclass
class ShareRideDTO:
    user_id: int
    from_place: str
    to_place: str
    date_time: datetime
    flexible_timings: bool
    start_date_time: datetime
    end_date_time: datetime
    no_of_seats_available: int
    assets_quantity: int
