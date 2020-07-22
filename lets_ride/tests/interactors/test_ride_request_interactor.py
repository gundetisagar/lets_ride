import datetime

import pytest
from freezegun import freeze_time
from unittest.mock import patch, Mock


from lets_ride.tests.factories.interactor_dtos import RideRequestDtoFactory
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.ride_request_interactor import RideRequestInteractor


@freeze_time("2020-07-22 05:21:34")
class TestRideRequest:

    @pytest.fixture()
    def storage_mock(self):
        from lets_ride.interactors.presenters.ride_request_presenter_interface \
            import RideRequestPresenterInterface
        from unittest.mock import create_autospec
        storage = create_autospec(RideRequestPresenterInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from lets_ride.interactors.presenters.ride_request_presenter_interface \
            import RideRequestPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(RideRequestPresenterInterface)
        return presenter

    def test_ride_requset_with_from_and_to_places_same_raises_exception(self,
                                                                        storage_mock,
                                                                        presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(from_place="kurnool", to_place="kurnool")
        interator = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_from_and_to_place_are_same.return_value = mock_object

        # Act
        response = interator.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_from_and_to_place_are_same.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_ride_requset_with_from_and_to_places_with_different_places(self,
                                                                        storage_mock,
                                                                        presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            datetime="2020-07-22 11:00:00"
        )
        interator = RideRequestInteractor(storage=storage_mock)

        # Act
        response = interator.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

    @freeze_time("2020-07-22 00:00:00")
    def test_datetime_is_not_past(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            flexible_timings= False,
            datetime="2020-07-21 11:00:00"
        )
        interator = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_from_and_to_place_are_same.return_value = mock_object

        # Act
        response = interator.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

    @freeze_time("2020-07-22 00:00:00")
    def test_start_datetime_is_less_than_end_datetime_raises_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            flexible_timings=True,
            start_datetime="2020-07-22 12:00:00",
            end_datetime="2020-07-22 11:00:00"
        )
        print(ride_request_dto)
        interator = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_end_datetime.return_value = mock_object

        # Act
        response = interator.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_end_datetime.assert_called_once()
