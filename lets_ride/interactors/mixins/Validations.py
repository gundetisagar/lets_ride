from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT


class ValidationMixin:

    def validate_from_and_to_places_not_same(self, from_place: str,
                                             to_place: str):
        if from_place == to_place:
            from lets_ride.exceptions.exceptions import InvalidToPlace
            raise InvalidToPlace

    def validate_date_time(self, date_time: str):
        import datetime
        date_time = datetime.datetime.strptime(date_time,
                                               DEFAULT_DATE_TIME_FORMAT)
        current_datetime = datetime.datetime.now()

        if current_datetime > date_time:
            from lets_ride.exceptions.exceptions import InvalidDatetime
            raise InvalidDatetime

    def validate_start_datetime_less_than_end_datetime(self,
                                                       start_date_time: str,
                                                       end_date_time: str):
        import datetime
        start_date_time = datetime.datetime.strptime(start_date_time,
                                                     DEFAULT_DATE_TIME_FORMAT)
        end_date_time = datetime.datetime.strptime(end_date_time,
                                                   DEFAULT_DATE_TIME_FORMAT)
        current_datetime = datetime.datetime.now()

        if current_datetime > start_date_time:
            from lets_ride.exceptions.exceptions import InvalidDatetime
            raise InvalidDatetime

        if start_date_time > end_date_time:
            from lets_ride.exceptions.exceptions import InvalidEndDatetime
            raise InvalidEndDatetime
