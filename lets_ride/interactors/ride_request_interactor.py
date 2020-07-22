from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT
from lets_ride.dtos.dtos import RideRequestDTO
from lets_ride.exceptions.exceptions import InvalidToPlace, InvalidDatetimeFormat, InvalidStartDatetimeFormat, \
    InvalidEndDatetimeFormat, InvalidDatetime, InvalidEndDatetime
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.presenters.ride_request_presenter_interface import RideRequestPresenterInterface
from lets_ride.interactors.storages.ride_request_storage_interface import RideRequestStorageInterface


class RideRequestInteractor(ValidationMixin):

    def __init__(self, storage: RideRequestStorageInterface):
        self.storage = storage

    def create_ride_request_wrapper(self, presenter: RideRequestPresenterInterface,
                                    ride_request_dto: RideRequestDTO):
        try:
            return self.create_ride_request(ride_request_dto=ride_request_dto, )
        except InvalidToPlace:
            return presenter.raise_exception_for_from_and_to_place_are_same()
        except InvalidEndDatetime:
            return presenter.raise_exception_for_invalid_end_datetime()

    def create_ride_request(self, ride_request_dto: RideRequestDTO):

        self.validate_from_and_to_places_not_same(
            from_place=ride_request_dto.from_place,
            to_place=ride_request_dto.to_place
        )
        if not ride_request_dto.flexible_timings:
            self.validate_datetime(datetime=ride_request_dto.datetime)

        if ride_request_dto.flexible_timings:
            self.validate_start_datetime_less_than_end_datetime(
                start_datetime=ride_request_dto.start_datetime,
                end_datetime=ride_request_dto.end_datetime
            )

# def validate_datetime_format(ride_request_dto: RideRequestDTO):
#     import datetime
#     if not ride_request_dto.flexible_timings:
#         try:
#             datetime.datetime.strptime(
#                 ride_request_dto.datetime, DEFAULT_DATE_TIME_FORMAT
#             )
#         except ValueError:
#             raise InvalidDatetimeFormat
#     else:
#         try:
#             datetime.datetime.strptime(
#                 ride_request_dto.start_datetime, DEFAULT_DATE_TIME_FORMAT
#             )
#         except ValueError:
#             raise InvalidStartDatetimeFormat
#         try:
#             datetime.datetime.strptime(
#                 ride_request_dto.end_datetime, DEFAULT_DATE_TIME_FORMAT
#             )
#         except ValueError:
#             raise InvalidEndDatetimeFormat

#
# def validate_datetime_is_in_future(ride_request_dto: RideRequestDTO):
#     print("inn")
#     import datetime
#     if not ride_request_dto.flexible_timings:
#         current_datetime = datetime.datetime.now() + datetime.timedelta(minutes=10)
#         if current_datetime >= ride_request_dto.datetime:
#             raise InvalidDatetime
#     else:
#         current_datetime = str(datetime.datetime.now() + datetime.timedelta(minutes=10))
#
#         if current_datetime < ride_request_dto.end_datetime:
#             raise InvalidEndDatetime
# except InvalidDatetimeFormat:
#     return presenter.raise_exception_for_invalid_datetime_format()
# except InvalidStartDatetimeFormat:
#     return presenter.raise_exception_for_invalid_start_datetime_format()
# except InvalidEndDatetimeFormat:
#     return presenter.raise_exception_for_invalid_end_datetime_format()
# except InvalidDatetime:
#     return presenter.raise_exception_for_datetime_is_in_past()
# except InvalidEndDatetime:
#     return presenter.raise_exception_for_invalid_end_datetime()
