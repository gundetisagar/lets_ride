from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.presenters.ride_request_presenter_implementation import RideRequestPresenterImplementation
from lets_ride.storages.ride_request_storage_implementation import RideRequestStorageImplementation
from ...dtos.dtos import RideRequestDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    print("*"*100)
    print(kwargs)
    user_id = kwargs["user"].id
    data = kwargs['request_data']
    ride_request_dto = RideRequestDTO(
        user_id=user_id,
        from_place=data["from_place"],
        to_place=data["to_place"],
        date_time=data["date_time"],
        luggage_quantity=data["luggage_quantity"],
        no_of_seats=data["no_of_seats"],
        flexible_timings=data["flexible_timings"],
        start_date_time=data["start_date_time"],
        end_date_time=data["end_date_time"]
    )

    ride_request_storage = RideRequestStorageImplementation()
    ride_request_presenter = RideRequestPresenterImplementation()
    interactor = RideRequestInteractor(
        storage=ride_request_storage
    )

    response = interactor.create_ride_request_wrapper(
        ride_request_dto=ride_request_dto, presenter=ride_request_presenter
    )
    return response

    # username = request_data['username']
    # password = request_data['password']
    # user_storage = UserStorageImplementation()
    # presenter = PresenterImplementation()
    # oauth_storage = OAuth2SQLStorage()
    #
    # interactor = LoginInteractor(
    #     user_storage=user_storage,
    #     oauth_storage=oauth_storage
    # )
    #
    # access_details = interactor.login_wrapper(
    #     username=username, password=password, presenter=presenter
    # )
    # return access_details

