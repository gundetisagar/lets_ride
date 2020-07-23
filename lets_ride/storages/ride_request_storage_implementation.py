from lets_ride.dtos.dtos import RideRequestDTO
from lets_ride.interactors.storages.ride_request_storage_interface import RideRequestStorageInterface


class RideRequestStorageImplementation(RideRequestStorageInterface):

    def create_ride_request(self, ride_request_dto: RideRequestDTO):
        from lets_ride.models.ride_request import RideRequest

        print(ride_request_dto.date_time)
        RideRequest.objects.create(
            user_id=ride_request_dto.user_id,
            from_place=ride_request_dto.from_place,
            to_place=ride_request_dto.to_place,
            flexible_timings=ride_request_dto.flexible_timings,
            date_time=ride_request_dto.date_time,
            start_date_time=ride_request_dto.start_date_time,
            end_date_time=ride_request_dto.end_date_time,
            no_of_seats=ride_request_dto.no_of_seats,
            luggage_quantity=ride_request_dto.luggage_quantity
        )