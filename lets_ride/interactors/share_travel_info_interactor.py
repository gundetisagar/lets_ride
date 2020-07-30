from lets_ride.dtos.dtos import ShareTravelInfoDTO
from lets_ride.exceptions.exceptions import InvalidToPlace, InvalidDatetime, \
    InvalidEndDatetime, InvalidAssetsQuantity
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.presenters.share_travel_info_presenter_interface \
    import ShareTravelInfoPresenterInterface
from lets_ride.interactors.storages.share_travel_info_storage_interface import \
    ShareTravelInfoStorageInterface


class ShareTravelInfoInteractor(ValidationMixin):

    def __init__(self, storage: ShareTravelInfoStorageInterface):
        self.storage = storage

    def create_ride_request_wrapper(self,
                                    presenter: ShareTravelInfoPresenterInterface,
                                    share_travel_info_dto: ShareTravelInfoDTO):
        try:
            self.create_share_travel_info(
                share_travel_info_dto=share_travel_info_dto
            )
        except InvalidToPlace:
            return presenter.raise_exception_for_from_and_to_place_are_same()
        except InvalidDatetime:
            return presenter.raise_exception_for_invalid_date_time()
        except InvalidEndDatetime:
            return presenter.raise_exception_for_invalid_end_datetime()
        except InvalidAssetsQuantity:
            return presenter.raise_exception_for_invalid_assets_quantity()

    def create_share_travel_info(self,
                                 share_travel_info_dto: ShareTravelInfoDTO):

        self.validate_from_and_to_places_not_same(
            from_place=share_travel_info_dto.from_place,
            to_place=share_travel_info_dto.to_place
        )

        if share_travel_info_dto.flexible_timings:
            self.validate_start_datetime_less_than_end_datetime(
                start_date_time=share_travel_info_dto.start_date_time,
                end_date_time=share_travel_info_dto.end_date_time
            )
        else:
            self.validate_date_time(date_time=share_travel_info_dto.date_time)

        self._validate_assets_quantity(
            assets_quantity=share_travel_info_dto.assets_quantity)

        self.storage.create_share_travel_info(
            share_travel_info_dto=share_travel_info_dto)

    @staticmethod
    def _validate_assets_quantity(assets_quantity: int):
        if assets_quantity < 0:
            from lets_ride.exceptions.exceptions import InvalidAssetsQuantity
            raise InvalidAssetsQuantity
