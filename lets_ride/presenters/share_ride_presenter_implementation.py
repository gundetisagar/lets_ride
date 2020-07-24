from lets_ride.interactors.presenters.share_ride_presenter_interface import \
    ShareRidePresenterInterface
import json

from django.http import response


class ShareRidePresenterImplementation(ShareRidePresenterInterface):

    def raise_exception_for_from_and_to_place_are_same(
            self) -> response.HttpResponse:
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

    def raise_exception_for_invalid_no_of_seats_available(
            self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import \
            INVALID_NO_OF_SEATS_AVAILABLE
        data = json.dumps({
            "response": INVALID_NO_OF_SEATS_AVAILABLE[0],
            "http_status_code": 400,
            "res_status": INVALID_NO_OF_SEATS_AVAILABLE[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def raise_exception_for_invalid_assets_quantity(
            self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import \
            INVALID_ASSETS_QUANTITY
        data = json.dumps({
            "response": INVALID_ASSETS_QUANTITY[0],
            "http_status_code": 400,
            "res_status": INVALID_ASSETS_QUANTITY[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object
