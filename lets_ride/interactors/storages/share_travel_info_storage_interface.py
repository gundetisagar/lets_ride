import abc

from lets_ride.dtos.dtos import ShareTravelInfoDTO


class ShareTravelInfoStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_share_travel_info(self,
                                 share_travel_info_dto: ShareTravelInfoDTO):
        pass
