from lets_ride.dtos.dtos import RideRequestDTO
from lets_ride.exceptions.exceptions import InvalidToPlace, InvalidDatetime, \
    InvalidEndDatetime, InvalidNoOfSeats, \
    InvalidLuggageQuantity
from lets_ride.interactors.dtos import MyRideRequestsQueryDTO
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

    def get_my_ride_requests_wrapper(self,
                                      my_ride_requests_query_dto: MyRideRequestsQueryDTO,
                                      presenter: RideRequestPresenterInterface):
        my_ride_requests_with_user_profile_dto = self._get_my_ride_requests(
            my_ride_requests_query_dto=my_ride_requests_query_dto
        )
        return presenter.my_ride_requests_response(
            my_ride_requests_with_user_profile_dto=my_ride_requests_with_user_profile_dto)

    def get_my_ride_requests(self,
                             my_ride_requests_query_dto: MyRideRequestsQueryDTO):
        self.validate_offset_value(my_ride_requests_query_dto.offset)
        self.validate_limit_value(my_ride_requests_query_dto.limit)
        ride_request_dtos = self.storage.get_my_ride_requests(
            my_ride_requests_query_dto=my_ride_requests_query_dto)
        list_of_user_ids = []
        for ride_request in ride_request_dtos:
            accepted_person = ride_request.accepted_person
            list_of_user_ids.append(accepted_person)

        from lets_ride.adapters.service_adapter import service_adapter
        service_adapter = service_adapter()
        user_profile_dtos = service_adapter.user_service.get_user_profile_dtos(
            user_ids=list_of_user_ids)
        from lets_ride.interactors.dtos import \
            MyRideRequestWithUserProfileDTO
        my_ride_requests_with_user_profile_dto = MyRideRequestWithUserProfileDTO(
            ride_request_dtos=ride_request_dtos,
            user_profile_dtos=user_profile_dtos
        )
        return my_ride_requests_with_user_profile_dto


