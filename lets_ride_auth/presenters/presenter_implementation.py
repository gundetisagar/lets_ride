from typing import List

from lets_ride_auth.dtos.dtos import UserProfileDTO
from lets_ride_auth.interactors.presenters.presenter_interface import \
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
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):

    def raise_exception_for_invalid_username(self) -> response.HttpResponse:
        data = {
            "response": INVALID_USERNAME[0],
            "http_status_code": 404,
            "res_status": INVALID_USERNAME[1]
        }
        return self.prepare_404_not_found_response(response_dict=data)

    def raise_exception_for_invalid_password(self):
        data = {
            "response": INVALID_PASSWORD[0],
            "http_status_code": 400,
            "res_status": INVALID_PASSWORD[1]
        }
        return self.prepare_400_bad_request_response(response_dict=data)

    def login_response(self, tokens_dto) -> response.HttpResponse:
        login_access_dict = {
            "user_id": tokens_dto.user_id,
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in": str(tokens_dto.expires_in)
        }
        return self.prepare_200_success_response(
            response_dict=login_access_dict)

    def get_users_profile_response(self, user_dtos: List[
        UserProfileDTO]) -> response.HttpResponse:
        list_of_user_dtos = []

        for user in user_dtos:
            user_profile_dict = {
                "user_id": user.user_id,
                "username": user.username,
                "name": user.name,
                "mobile_number": user.mobile_number
            }
            list_of_user_dtos.append(user_profile_dict)
        return self.prepare_200_success_response(
            response_dict=list_of_user_dtos)
