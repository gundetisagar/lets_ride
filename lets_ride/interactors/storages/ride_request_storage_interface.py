from abc import ABC
from abc import abstractmethod

from lets_ride.dtos.dtos import RideRequestDTO


class RideRequestStorageInterface(ABC):

    @abstractmethod
    def create_ride_request(self, ride_request_dto: RideRequestDTO):
        pass
