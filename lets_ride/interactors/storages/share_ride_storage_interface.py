from abc import ABC
from abc import abstractmethod

from lets_ride.dtos.dtos import ShareRideDTO


class ShareRideStorageInterface(ABC):

    @abstractmethod
    def create_share_ride(self, share_ride_dto: ShareRideDTO):
        pass
