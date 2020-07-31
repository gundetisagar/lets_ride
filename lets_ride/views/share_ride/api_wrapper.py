from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...dtos.dtos import ShareRideDTO
from ...interactors.share_ride_interactor import ShareRideInteractor
from ...presenters.share_ride_presenter_implementation import \
    ShareRidePresenterImplementation
from ...storages.share_ride_storage_implementation import \
    ShareRideStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs["user"].id
    data = kwargs['request_data']
    share_ride_dto = ShareRideDTO(
        user_id=user_id,
        from_place=data["from_place"],
        to_place=data["to_place"],
        date_time=data["date_time"],
        assets_quantity=data["assets_quantity"],
        no_of_seats_available=data["no_of_seats_available"],
        flexible_timings=data["flexible_timings"],
        start_date_time=data["start_date_time"],
        end_date_time=data["end_date_time"]
    )

    share_ride_storage = ShareRideStorageImplementation()
    share_ride_presenter = ShareRidePresenterImplementation()
    interactor = ShareRideInteractor(
        storage=share_ride_storage
    )

    response = interactor.create_share_ride_wrapper(
        share_ride_dto=share_ride_dto, presenter=share_ride_presenter
    )
    return response
