from lets_ride.dtos.dtos import AssetTransportRequestDTO
from lets_ride.interactors.storages.asset_transport_request_storage_interface \
    import AssetTransportRequestStorageInterface


class AssetTransportRequestStorageImplementation(
    AssetTransportRequestStorageInterface):

    def create_asset_transport_request(
            self, asset_transport_request_dto: AssetTransportRequestDTO):
        from lets_ride.models.asset_transport_request import \
            AssetTransportRequest

        AssetTransportRequest.objects.create(
            user_id=asset_transport_request_dto.user_id,
            from_place=asset_transport_request_dto.from_place,
            to_place=asset_transport_request_dto.to_place,
            flexible_timings=asset_transport_request_dto.flexible_timings,
            date_time=asset_transport_request_dto.date_time,
            start_date_time=asset_transport_request_dto.start_date_time,
            end_date_time=asset_transport_request_dto.end_date_time,
            no_of_assets=asset_transport_request_dto.no_of_assets,
            asset_type=asset_transport_request_dto.asset_type,
            others=asset_transport_request_dto.others,
            asset_sensitivity=asset_transport_request_dto.asset_sensitivity,
            whom_to_deliver=asset_transport_request_dto.whom_to_deliver
        )
