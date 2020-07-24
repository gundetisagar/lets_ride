from lets_ride.dtos.dtos import ShareRideDTO
from lets_ride.exceptions.exceptions import InvalidToPlace, InvalidDatetime, \
    InvalidEndDatetime, InvalidNoOfSeatsAvailable, InvalidAssetsQuantity
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.presenters.share_ride_presenter_interface import \
    ShareRidePresenterInterface
from lets_ride.interactors.storages.share_ride_storage_interface import \
    ShareRideStorageInterface


class ShareRideInteractor(ValidationMixin):

    def __init__(self, storage: ShareRideStorageInterface):
        self.storage = storage

    def create_share_ride_wrapper(self,
                                  presenter: ShareRidePresenterInterface,
                                  share_ride_dto: ShareRideDTO):
        try:
            self.create_share_ride(share_ride_dto=share_ride_dto)
        except InvalidToPlace:
            return presenter.raise_exception_for_from_and_to_place_are_same()
        except InvalidDatetime:
            print("inter")
            data = presenter.raise_exception_for_invalid_date_time()
            print(data)
            return data
        except InvalidEndDatetime:
            return presenter.raise_exception_for_invalid_end_datetime()
        except InvalidNoOfSeatsAvailable:
            return presenter.raise_exception_for_invalid_no_of_seats_available()
        except InvalidAssetsQuantity:
            return presenter.raise_exception_for_invalid_assets_quantity()

    def create_share_ride(self, share_ride_dto: ShareRideDTO):

        self.validate_from_and_to_places_not_same(
            from_place=share_ride_dto.from_place,
            to_place=share_ride_dto.to_place
        )

        if share_ride_dto.flexible_timings:
            self.validate_start_datetime_less_than_end_datetime(
                start_date_time=share_ride_dto.start_date_time,
                end_date_time=share_ride_dto.end_date_time
            )
        else:
            self.validate_date_time(date_time=share_ride_dto.date_time)

        self._validate_assets_quantity(
            assets_quantity=share_ride_dto.assets_quantity)

        self._validate_no_of_seats_available(
            no_of_seats_available=share_ride_dto.no_of_seats_available)

        self.storage.create_share_ride(share_ride_dto=share_ride_dto)

    @staticmethod
    def _validate_no_of_seats_available(no_of_seats_available: int):
        if no_of_seats_available <= 0:
            from lets_ride.exceptions.exceptions import \
                InvalidNoOfSeatsAvailable
            raise InvalidNoOfSeatsAvailable

    @staticmethod
    def _validate_assets_quantity(assets_quantity: int):
        if assets_quantity < 0:
            from lets_ride.exceptions.exceptions import InvalidAssetsQuantity
            raise InvalidAssetsQuantity
