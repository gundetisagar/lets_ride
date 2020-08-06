from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from common.oauth2_storage import OAuth2SQLStorage
from .validator_class import ValidatorClass
from ...interactors.login_interactor import LoginInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']

    username = request_data['username']
    password = request_data['password']
    user_storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()

    interactor = LoginInteractor(
        user_storage=user_storage,
        oauth_storage=oauth_storage
    )

    access_details = interactor.login_wrapper(
        username=username, password=password, presenter=presenter
    )
    return access_details
