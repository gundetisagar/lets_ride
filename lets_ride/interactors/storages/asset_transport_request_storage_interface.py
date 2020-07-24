from abc import ABC
from abc import abstractmethod

from django.http import HttpResponse

from lets_ride.dtos.dtos import AssetTransportRequestDTO


class AssetTransportRequestStorageInterface(ABC):

    def create_asset_transport_request(
            self, asset_transport_request_dto: AssetTransportRequestDTO):

        pass
