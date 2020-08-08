import datetime as datetime

from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT
import datetime


class ValidationMixin:

    def validate_from_and_to_places_not_same(self, from_place: str,
                                             to_place: str):
        if from_place == to_place:
            from lets_ride.exceptions.exceptions import InvalidToPlace
            raise InvalidToPlace

    def validate_date_time(self, date_time: datetime.datetime):
        current_datetime = datetime.datetime.now()
        if current_datetime > date_time:
            from lets_ride.exceptions.exceptions import InvalidDatetime
            raise InvalidDatetime

    def validate_start_datetime_less_than_end_datetime(
            self, start_date_time: datetime.datetime,
            end_date_time: datetime.datetime):

        import datetime
        current_datetime = datetime.datetime.now()

        if current_datetime > start_date_time:
            from lets_ride.exceptions.exceptions import InvalidDatetime
            raise InvalidDatetime

        if start_date_time > end_date_time:
            from lets_ride.exceptions.exceptions import InvalidEndDatetime
            raise InvalidEndDatetime

    def validate_offset_value(self, offset: int):
        if offset < 0:
            from lets_ride.exceptions.exceptions import InvalidOffsetValue
            raise InvalidOffsetValue

    def validate_limit_value(self, limit: int):
        if limit <= 0:
            from lets_ride.exceptions.exceptions import InvalidLimitValue
            raise InvalidLimitValue
