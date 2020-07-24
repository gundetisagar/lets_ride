from lets_ride.interactors.presenters.ride_request_presenter_interface import \
    RideRequestPresenterInterface
import json

from django.http import response


class RideRequestPresenterImplementation(RideRequestPresenterInterface):

    def raise_exception_for_from_and_to_place_are_same(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_TO_PLACE
        data = json.dumps({
            "response": INVALID_TO_PLACE[0],
            "http_status_code": 400,
            "res_status": INVALID_TO_PLACE[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def raise_exception_for_invalid_date_time(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_DATE_TIME
        data = json.dumps({
            "response": INVALID_DATE_TIME[0],
            "http_status_code": 400,
            "res_status": INVALID_DATE_TIME[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def raise_exception_for_invalid_end_datetime(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_END_DATETIME
        data = json.dumps({
            "response": INVALID_END_DATETIME[0],
            "http_status_code": 400,
            "res_status": INVALID_END_DATETIME[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def raise_exception_for_invalid_no_of_seats(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_NO_OF_ASSETS
        data = json.dumps({
            "response": INVALID_NO_OF_ASSETS[0],
            "http_status_code": 400,
            "res_status": INVALID_NO_OF_ASSETS[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def raise_exception_for_invalid_luggage_quantity(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_LUGGAGE_QUANTITY
        data = json.dumps({
            "response": INVALID_LUGGAGE_QUANTITY[0],
            "http_status_code": 400,
            "res_status": INVALID_LUGGAGE_QUANTITY[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object
