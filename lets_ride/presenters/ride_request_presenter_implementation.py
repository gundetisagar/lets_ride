from lets_ride.interactors.presenters.ride_request_presenter_interface import \
    RideRequestPresenterInterface
import json

from django.http import response
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin


class RideRequestPresenterImplementation(RideRequestPresenterInterface,
                                         HTTPResponseMixin):

    def raise_exception_for_from_and_to_place_are_same(
            self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_TO_PLACE
        response_dict = {
            "response": INVALID_TO_PLACE[0],
            "http_status_code": 400,
            "res_status": INVALID_TO_PLACE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_exception_for_invalid_date_time(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_DATE_TIME
        response_dict = {
            "response": INVALID_DATE_TIME[0],
            "http_status_code": 400,
            "res_status": INVALID_DATE_TIME[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_exception_for_invalid_end_datetime(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_END_DATETIME
        response_dict = {
            "response": INVALID_END_DATETIME[0],
            "http_status_code": 400,
            "res_status": INVALID_END_DATETIME[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_exception_for_invalid_no_of_seats(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_NO_OF_SEATS
        response_dict = {
            "response": INVALID_NO_OF_SEATS[0],
            "http_status_code": 400,
            "res_status": INVALID_NO_OF_SEATS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_exception_for_invalid_luggage_quantity(
            self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import \
            INVALID_LUGGAGE_QUANTITY
        response_dict = {
            "response": INVALID_LUGGAGE_QUANTITY[0],
            "http_status_code": 400,
            "res_status": INVALID_LUGGAGE_QUANTITY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
