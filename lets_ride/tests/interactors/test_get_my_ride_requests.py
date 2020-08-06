from unittest.mock import Mock

import pytest

from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.interactors.storages.ride_request_storage_interface import \
    RideRequestStorageInterface


class TestMyRideRequests:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from lets_ride.interactors.storages.ride_request_storage_interface import \
            RideRequestStorageInterface
        storage = create_autospec(RideRequestStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from lets_ride.interactors.presenters.ride_request_presenter_interface \
            import RideRequestPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(RideRequestPresenterInterface)
        return presenter

    def test_get_my_ride_requests(self, storage_mock, presenter_mock):
        # Arrange
        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
