import pytest
from freezegun import freeze_time
from unittest.mock import patch, Mock

from lets_ride.tests.factories.interactor_dtos import RideRequestDtoFactory
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.ride_request_interactor import RideRequestInteractor


class TestRideRequest:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from lets_ride.interactors.storages.ride_request_storage_interface import RideRequestStorageInterface
        storage = create_autospec(RideRequestStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from lets_ride.interactors.presenters.ride_request_presenter_interface \
            import RideRequestPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(RideRequestPresenterInterface)
        return presenter

    @freeze_time("2020-07-22 00:00:00")
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
            date_time="2020-07-22 11:00:00"
        )
        interator = RideRequestInteractor(storage=storage_mock)

        # Act
        response = interator.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )
        # Assert
        presenter_mock.raise_exception_for_from_and_to_place_are_same.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_date_time_is_in_past_raise_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            flexible_timings=False,
            date_time="2020-07-21 11:00:00"
        )
        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_date_time.return_value = mock_object

        # Act
        response = interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )
        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_date_time.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_given_date_time_is_greater_than_current_datetime_did_not_raise_exception(self, storage_mock,
                                                                                      presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            flexible_timings=False,
            date_time="2020-07-22 01:00:00"
        )
        interactor = RideRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )
        presenter_mock.raise_exception_for_invalid_date_time.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_end_datetime_is_less_than_start_datetime_raises_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            flexible_timings=True,
            start_date_time="2020-07-22 12:00:00",
            end_date_time="2020-07-22 11:00:00"
        )

        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_end_datetime.return_value = mock_object

        # Act
        response = interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_end_datetime.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_start_datetime_less_than_end_datetime_did_not_raises_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            flexible_timings=True,
            start_date_time="2020-07-22 12:00:00",
            end_date_time="2020-07-22 13:00:00"
        )
        interactor = RideRequestInteractor(storage=storage_mock)

        # Act
        response = interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_end_datetime.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_seats_equals_to_zero_raise_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            no_of_seats=0
        )
        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_no_of_seats.return_value = mock_object
        # Act
        response = interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_no_of_seats.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_seats_is_negative_raise_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            no_of_seats=-1
        )
        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_no_of_seats.return_value = mock_object
        # Act
        response = interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_no_of_seats.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_seats_is_positive_did_not_raise_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            no_of_seats=1
        )
        interactor = RideRequestInteractor(storage=storage_mock)

        # Act
        response = interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_no_of_seats.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_luggage_quantity_is_negative_raise_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            luggage_quantity=-1
        )
        interactor = RideRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_luggage_quantity.return_value = mock_object
        # Act
        response = interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_luggage_quantity.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_luggage_quantity_is_zero_did_not_raise_exception(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            no_of_seats=0
        )
        interactor = RideRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_luggage_quantity.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_false_and_create_ride_request(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=False,
            date_time="2020-07-22 05:00:00"
        )
        interactor = RideRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_ride_request.assert_called_once_with(ride_request_dto=ride_request_dto)

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_true_and_create_ride_request(self, storage_mock, presenter_mock):
        # Arrange
        ride_request_dto = RideRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=True,
            date_time=None,
            start_date_time="2020-07-22 01:00:00",
            end_date_time="2020-07-22 05:00:00"
        )
        interactor = RideRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_ride_request_wrapper(
            ride_request_dto=ride_request_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_ride_request.assert_called_once_with(ride_request_dto=ride_request_dto)
