from unittest.mock import Mock

import pytest

from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.interactors.storages.ride_request_storage_interface import \
    RideRequestStorageInterface
from lets_ride.tests.interactors.dtos import \
    MyRideRequestWithUserProfileDtoFactory


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

    def test_get_my_ride_requests_with_offset_is_negative_raises_exception(
            self, storage_mock,
            presenter_mock):
        # Arrange
        from lets_ride.tests.factories.interactor_dtos import \
            MyRideRequestsQueryDtoFactory
        my_ride_requests_query_dto = MyRideRequestsQueryDtoFactory(
            offset=-1
        )

        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_offset_value. \
            return_value = mock_object

        # Act
        return_response = interactor.get_my_ride_requests_wrapper(
            my_ride_requests_query_dto=my_ride_requests_query_dto,
            presenter=presenter_mock)

        # Assert
        assert return_response == mock_object
        presenter_mock.raise_exception_for_invalid_offset_value.assert_called_once()

    def test_get_my_ride_requests_with_limit_is_0_raises_exception(
            self, storage_mock,
            presenter_mock):
        # Arrange
        from lets_ride.tests.factories.interactor_dtos import \
            MyRideRequestsQueryDtoFactory
        my_ride_requests_query_dto = MyRideRequestsQueryDtoFactory(
            limit=0
        )

        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_limit_value. \
            return_value = mock_object

        # Act
        return_response = interactor.get_my_ride_requests_wrapper(
            my_ride_requests_query_dto=my_ride_requests_query_dto,
            presenter=presenter_mock)

        # Assert
        assert return_response == mock_object
        presenter_mock.raise_exception_for_invalid_limit_value.assert_called_once()

    def test_get_my_ride_requests_with_limit_value_is_negative_raises_exception(
            self, storage_mock,
            presenter_mock):
        # Arrange
        from lets_ride.tests.factories.interactor_dtos import \
            MyRideRequestsQueryDtoFactory
        my_ride_requests_query_dto = MyRideRequestsQueryDtoFactory(
            limit=-1
        )

        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_limit_value. \
            return_value = mock_object

        # Act
        return_response = interactor.get_my_ride_requests_wrapper(
            my_ride_requests_query_dto=my_ride_requests_query_dto,
            presenter=presenter_mock)

        # Assert
        assert return_response == mock_object
        presenter_mock.raise_exception_for_invalid_limit_value.assert_called_once()

    def test_get_my_ride_requests_with_valid_values_return_response(
            self, storage_mock,
            presenter_mock):
        # Arrange
        from lets_ride.tests.factories.interactor_dtos import \
            MyRideRequestsQueryDtoFactory
        my_ride_requests_query_dto = MyRideRequestsQueryDtoFactory()
        expected_my_ride_requests = MyRideRequestWithUserProfileDtoFactory()

        interactor = RideRequestInteractor(storage=storage_mock)
        storage_mock.get_my_ride_requests.return_value = expected_my_ride_requests

        # Act
        return_response = interactor.get_my_ride_requests_wrapper(
            my_ride_requests_query_dto=my_ride_requests_query_dto,
            presenter=presenter_mock)

        # Assert
        assert return_response == expected_my_ride_requests
