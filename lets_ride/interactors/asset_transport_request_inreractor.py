from lets_ride.dtos.dtos import AssetTransportRequestDTO
from lets_ride.exceptions.exceptions import InvalidToPlace, InvalidDatetime, \
    InvalidEndDatetime, InvalidNoOfAssets, InvalidOthersField, \
    InvalidWhomToDeliver
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.presenters.asset_transport_request_presenter_interface \
    import AssetTransportRequestPresenterInterface
from lets_ride.interactors.storages.asset_transport_request_storage_interface \
    import AssetTransportRequestStorageInterface


class AssetTransportRequestInteractor(ValidationMixin):

    def __init__(self, storage: AssetTransportRequestStorageInterface):
        self.storage = storage

    def create_asset_transport_request_wrapper(
            self, presenter: AssetTransportRequestPresenterInterface,
            asset_transport_request_dto: AssetTransportRequestDTO):
        try:
            self.create_asset_transport_request(
                asset_transport_request_dto=asset_transport_request_dto)
        except InvalidToPlace:
            return presenter.raise_exception_for_from_and_to_place_are_same()
        except InvalidDatetime:
            return presenter.raise_exception_for_invalid_date_time()
        except InvalidEndDatetime:
            return presenter.raise_exception_for_invalid_end_datetime()
        except InvalidNoOfAssets:
            return presenter.raise_exception_for_invalid_no_of_assets()
        except InvalidWhomToDeliver:
            return presenter.raise_exception_for_invalid_whom_to_deliver()

    def create_asset_transport_request(
            self, asset_transport_request_dto: AssetTransportRequestDTO):

        self.validate_from_and_to_places_not_same(
            from_place=asset_transport_request_dto.from_place,
            to_place=asset_transport_request_dto.to_place
        )

        if asset_transport_request_dto.flexible_timings:
            self.validate_start_datetime_less_than_end_datetime(
                start_date_time=asset_transport_request_dto.start_date_time,
                end_date_time=asset_transport_request_dto.end_date_time
            )
        else:
            self.validate_date_time(
                date_time=asset_transport_request_dto.date_time)

        self._validate_no_of_assets(
            no_of_assets=asset_transport_request_dto.no_of_assets)

        self._validate_whom_to_deliver(
            whom_to_deliver=asset_transport_request_dto.whom_to_deliver
        )

        self.storage.create_asset_transport_request(
            asset_transport_request_dto=asset_transport_request_dto)

    @staticmethod
    def _validate_no_of_assets(no_of_assets: int):
        if no_of_assets <= 0:
            raise InvalidNoOfAssets

    @staticmethod
    def _validate_whom_to_deliver(whom_to_deliver: str):
        if len(whom_to_deliver) <= 12:
            raise InvalidWhomToDeliver
