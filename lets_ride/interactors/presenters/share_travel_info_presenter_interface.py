import abc
from django.http import HttpResponse


class ShareTravelInfoPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_exception_for_from_and_to_place_are_same(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_date_time(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_end_datetime(self) -> HttpResponse:
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_assets_quantity(self) -> HttpResponse:
        pass
