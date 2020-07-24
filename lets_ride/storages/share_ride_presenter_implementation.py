from lets_ride.dtos.dtos import ShareRideDTO
from lets_ride.interactors.storages.share_ride_storage_interface import ShareRideStorageInterface


class ShareRideStorageImplementation(ShareRideStorageInterface):

    def create_share_ride(self, share_ride_dto: ShareRideDTO):
        from lets_ride.models.share_ride import ShareRide

        ShareRide.objects.create(
            user_id=share_ride_dto.user_id,
            from_place=share_ride_dto.from_place,
            to_place=share_ride_dto.to_place,
            flexible_timings=share_ride_dto.flexible_timings,
            date_time=share_ride_dto.date_time,
            start_date_time=share_ride_dto.start_date_time,
            end_date_time=share_ride_dto.end_date_time,
            no_of_seats_available=share_ride_dto.no_of_seats_available,
            assets_quantity=share_ride_dto.assets_quantity
        )