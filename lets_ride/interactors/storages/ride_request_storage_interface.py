from abc import ABC
from abc import abstractmethod
from typing import List

from lets_ride.dtos.dtos import RideRequestDTO
from lets_ride.interactors.dtos import MyRideRequestsQueryDTO
from lets_ride.interactors.dtos import MyRideRequestDTO


class RideRequestStorageInterface(ABC):

    @abstractmethod
    def create_ride_request(self, ride_request_dto: RideRequestDTO):
        pass

    @abstractmethod
    def get_my_ride_requests(self,
                             my_ride_requests_query_dto: MyRideRequestsQueryDTO) -> \
    List[MyRideRequestDTO]:
        pass
