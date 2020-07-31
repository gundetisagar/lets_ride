from lets_ride.dtos.dtos import ShareTravelInfoDTO
from lets_ride.interactors.storages.share_travel_info_storage_interface import \
    ShareTravelInfoStorageInterface
from lets_ride.models import ShareTravelInfo


class ShareTravelInfoStorageImplementation(ShareTravelInfoStorageInterface):

    def create_share_travel_info(self,
                                 share_travel_info_dto: ShareTravelInfoDTO):
        ShareTravelInfo.objects.create(
            user_id=share_travel_info_dto.user_id,
            from_place=share_travel_info_dto.from_place,
            to_place=share_travel_info_dto.to_place,
            flexible_timings=share_travel_info_dto.flexible_timings,
            date_time=share_travel_info_dto.date_time,
            start_date_time=share_travel_info_dto.start_date_time,
            end_date_time=share_travel_info_dto.end_date_time,
            assets_quantity=share_travel_info_dto.assets_quantity
        )
