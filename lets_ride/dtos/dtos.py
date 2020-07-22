import dataclasses
from typing import Optional

import datetime


@dataclasses.dataclass
class RideRequestDTO:
    user_id: int
    from_place: str
    to_place: str
    datetime: datetime
    flexible_timings: bool
    start_datetime: datetime
    end_datetime: datetime
    no_of_seats: int
    luggage_quantity: int
