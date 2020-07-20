from lets_ride.interactors.presenters.presenter_interface import \
    PresenterInterface
from lets_ride_auth.constants.exception_messages import (
    INVALID_USERNAME,
    INVALID_PASSWORD
)
# from lets_ride_auth.exceptions.exceptions import (
#     InvalidUsername,
#     InvalidPassword
# )

from django.http import response


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_username(self) -> response.HttpResponse:
        import json
        data = json.dumps({
            "response": INVALID_USERNAME[0],
            "http_status_code": 404,
            "res_status": INVALID_USERNAME[1]
        })
        response_object = response.HttpResponse(data, 404)
        return response_object

    def raise_exception_for_invalid_password(self):
        import json
        data = json.dumps({
            "response": INVALID_PASSWORD[0],
            "http_status_code": 404,
            "res_status": INVALID_PASSWORD[1]
        })
        response_object = response.HttpResponse(data, 404)
        return response_object

    def user_login_response(self, tokens_dto):
        login_access_dict = {
            "user_id": tokens_dto.user_id,
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in": tokens_dto.expires_in

        }
        return login_access_dict
