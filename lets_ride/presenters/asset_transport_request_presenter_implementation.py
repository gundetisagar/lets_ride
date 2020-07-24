from lets_ride.interactors.presenters.asset_transport_request_presenter_interface \
    import AssetTransportRequestPresenterInterface
import json

from django.http import response
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin


class AssetTransportRequestPresenterImplementation(
    AssetTransportRequestPresenterInterface, HTTPResponseMixin):

    def raise_exception_for_from_and_to_place_are_same(
            self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_TO_PLACE
        response = {
            "response": INVALID_TO_PLACE[0],
            "http_status_code": 400,
            "res_status": INVALID_TO_PLACE[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response)

    def raise_exception_for_invalid_date_time(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_DATE_TIME
        response = {
            "response": INVALID_DATE_TIME[0],
            "http_status_code": 400,
            "res_status": INVALID_DATE_TIME[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response)

    def raise_exception_for_invalid_end_datetime(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_END_DATETIME
        response = {
            "response": INVALID_END_DATETIME[0],
            "http_status_code": 400,
            "res_status": INVALID_END_DATETIME[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response)

    def raise_exception_for_invalid_no_of_assets(self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import INVALID_NO_OF_ASSETS
        response = {
            "response": INVALID_NO_OF_ASSETS[0],
            "http_status_code": 400,
            "res_status": INVALID_NO_OF_ASSETS[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response)

    def raise_exception_for_invalid_whom_to_deliver(
            self) -> response.HttpResponse:
        from lets_ride.constants.exception_messages import \
            INVALID_WHOM_TO_DELIVER
        response = {
            "response": INVALID_WHOM_TO_DELIVER[0],
            "http_status_code": 400,
            "res_status": INVALID_WHOM_TO_DELIVER[1]
        }
        return self.prepare_400_bad_request_response(response_dict=response)
