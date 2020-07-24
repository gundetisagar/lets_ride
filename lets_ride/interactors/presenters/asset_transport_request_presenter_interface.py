from abc import ABC
from abc import abstractmethod

from django.http import HttpResponse


class AssetTransportRequestPresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_from_and_to_place_are_same(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_date_time(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_end_datetime(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_no_of_assets(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_whom_to_deliver(self) -> HttpResponse:
        pass