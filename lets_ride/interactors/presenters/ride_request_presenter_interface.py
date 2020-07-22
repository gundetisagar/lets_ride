from abc import ABC
from abc import abstractmethod

from django.http import HttpResponse


class RideRequestPresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_from_and_to_place_are_same(self) -> HttpResponse:
        pass

    @abstractmethod
    def raise_exception_for_invalid_end_datetime(self) -> HttpResponse:
        pass

    # @abstractmethod
    # def raise_exception_for_invalid_datetime_format(self) -> HttpResponse:
    #     pass
    #
    # @abstractmethod
    # def raise_exception_for_invalid_start_datetime_format(self) -> HttpResponse:
    #     pass
    #
    # @abstractmethod
    # def raise_exception_for_invalid_end_datetime_format(self) -> HttpResponse:
    #     pass
    #
    # @abstractmethod
    # def raise_exception_for_datetime_is_in_past(self) -> HttpResponse:
    #     pass
    #
