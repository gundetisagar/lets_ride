from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT


class ValidationMixin:

    def validate_from_and_to_places_not_same(self, from_place: str, to_place: str):
        if from_place == to_place:
            from lets_ride.exceptions.exceptions import InvalidToPlace
            raise InvalidToPlace
        return True

    def validate_datetime(self, date_time: str):
        import datetime
        print(datetime)
        date_time = datetime.datetime.strptime(datetime, DEFAULT_DATE_TIME_FORMAT)
        current_datetime = datetime.datetime.now()
        print(date_time)
        print(current_datetime)


    def validate_start_datetime_less_than_end_datetime(self, start_datetime: str, end_datetime: str):
        import datetime
        start_datetime = datetime.datetime.strptime(start_datetime, DEFAULT_DATE_TIME_FORMAT)
        end_datetime = datetime.datetime.strptime(end_datetime, DEFAULT_DATE_TIME_FORMAT)

        if start_datetime > end_datetime:
            from lets_ride.exceptions.exceptions import InvalidEndDatetime
            raise InvalidEndDatetime

