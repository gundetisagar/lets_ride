from lets_ride.dtos.dtos import RideRequestDTO
from lets_ride.exceptions.exceptions import InvalidToPlace, InvalidDatetime, \
    InvalidEndDatetime, InvalidNoOfSeats, \
    InvalidLuggageQuantity
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.presenters.ride_request_presenter_interface import \
    RideRequestPresenterInterface
from lets_ride.interactors.storages.ride_request_storage_interface import \
    RideRequestStorageInterface


class RideRequestInteractor(ValidationMixin):

    def __init__(self, storage: RideRequestStorageInterface):
        self.storage = storage

    def create_ride_request_wrapper(self,
                                    presenter: RideRequestPresenterInterface,
                                    ride_request_dto: RideRequestDTO):
        try:
            self.create_ride_request(ride_request_dto=ride_request_dto)
        except InvalidToPlace:
            return presenter.raise_exception_for_from_and_to_place_are_same()
        except InvalidDatetime:
            return presenter.raise_exception_for_invalid_date_time()
        except InvalidEndDatetime:
            return presenter.raise_exception_for_invalid_end_datetime()
        except InvalidNoOfSeats:
            return presenter.raise_exception_for_invalid_no_of_seats()
        except InvalidLuggageQuantity:
            return presenter.raise_exception_for_invalid_luggage_quantity()

    def create_ride_request(self, ride_request_dto: RideRequestDTO):

        self.validate_from_and_to_places_not_same(
            from_place=ride_request_dto.from_place,
            to_place=ride_request_dto.to_place
        )

        if ride_request_dto.flexible_timings:
            self.validate_start_datetime_less_than_end_datetime(
                start_date_time=ride_request_dto.start_date_time,
                end_date_time=ride_request_dto.end_date_time
            )
        else:
            self.validate_date_time(date_time=ride_request_dto.date_time)

        self._validate_luggage_quantity(
            luggage_quantity=ride_request_dto.luggage_quantity)

        self._validate_no_of_seats(
            no_of_seats=ride_request_dto.no_of_seats)

        self.storage.create_ride_request(ride_request_dto=ride_request_dto)


    @staticmethod
    def _validate_no_of_seats(no_of_seats: int):
        if no_of_seats <= 0:
            from lets_ride.exceptions.exceptions import InvalidNoOfSeats
            raise InvalidNoOfSeats


    @staticmethod
    def _validate_luggage_quantity(luggage_quantity: int):
        if luggage_quantity < 0:
            from lets_ride.exceptions.exceptions import InvalidLuggageQuantity
            raise InvalidLuggageQuantity
