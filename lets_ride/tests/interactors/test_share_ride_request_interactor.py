import pytest
from freezegun import freeze_time
from unittest.mock import patch, Mock

from lets_ride.tests.factories.interactor_dtos import ShareRideDtoFactory
from lets_ride.interactors.share_ride_interactor import ShareRideInteractor


class TestShareRide:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from lets_ride.interactors.storages.share_ride_storage_interface import \
            ShareRideStorageInterface
        storage = create_autospec(ShareRideStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from lets_ride.interactors.presenters.share_ride_presenter_interface \
            import ShareRidePresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(ShareRidePresenterInterface)
        return presenter

    @freeze_time("2020-07-22 00:00:00")
    def test_with_from_and_to_places_same_raises_exception(self,
                                                           storage_mock,
                                                           presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(from_place="kurnool",
                                             to_place="kurnool")
        interator = ShareRideInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_from_and_to_place_are_same.return_value = mock_object

        # Act
        response = interator.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_from_and_to_place_are_same.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_with_from_and_to_places_with_different_places(self,
                                                           storage_mock,
                                                           presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            date_time="2020-07-22 11:00:00"
        )
        interator = ShareRideInteractor(storage=storage_mock)

        # Act
        response = interator.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )
        # Assert
        presenter_mock.raise_exception_for_from_and_to_place_are_same.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_date_time_is_in_past_raise_exception(self, storage_mock,
                                                  presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            flexible_timings=False,
            date_time="2020-07-21 11:00:00"
        )
        interactor = ShareRideInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_date_time.return_value = mock_object

        # Act
        response = interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )
        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_date_time.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_given_date_time_is_greater_than_current_datetime_did_not_raise_exception(
            self, storage_mock,
            presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            flexible_timings=False,
            date_time="2020-07-22 01:00:00"
        )
        interactor = ShareRideInteractor(storage=storage_mock)

        # Act
        interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )
        presenter_mock.raise_exception_for_invalid_date_time.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_end_datetime_is_less_than_start_datetime_raises_exception(self,
                                                                       storage_mock,
                                                                       presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            flexible_timings=True,
            start_date_time="2020-07-22 12:00:00",
            end_date_time="2020-07-22 11:00:00"
        )

        interactor = ShareRideInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_end_datetime.return_value = mock_object

        # Act
        response = interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_end_datetime.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_start_datetime_less_than_end_datetime_did_not_raises_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            flexible_timings=True,
            start_date_time="2020-07-22 12:00:00",
            end_date_time="2020-07-22 13:00:00"
        )
        interactor = ShareRideInteractor(storage=storage_mock)

        # Act
        response = interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_end_datetime.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_seats_available_equals_to_zero_raise_exception(self,
                                                                  storage_mock,
                                                                  presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            no_of_seats_available=0
        )
        interactor = ShareRideInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_no_of_seats_available.return_value = mock_object
        # Act
        response = interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_no_of_seats_available.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_seats_available_is_negative_raise_exception(self, storage_mock,
                                                     presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            no_of_seats_available=-1
        )
        interactor = ShareRideInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_no_of_seats_available.return_value = mock_object
        # Act
        response = interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_no_of_seats_available.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_seats_available_is_positive_did_not_raise_exception(self, storage_mock,
                                                             presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            no_of_seats_available=1
        )
        interactor = ShareRideInteractor(storage=storage_mock)

        # Act
        response = interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_no_of_seats_available.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_assets_quantity_is_negative_raise_exception(self, storage_mock,
                                                          presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            assets_quantity=-1
        )
        interactor = ShareRideInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_assets_quantity.return_value = mock_object
        # Act
        response = interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_assets_quantity.assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_assets_quantity_is_zero_did_not_raise_exception(self,
                                                              storage_mock,
                                                              presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            assets_quantity=0
        )
        interactor = ShareRideInteractor(storage=storage_mock)

        # Act
        interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_assets_quantity.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_false_and_create_share_ride(self,
                                                               storage_mock,
                                                               presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=False,
            date_time="2020-07-22 05:00:00"
        )
        interactor = ShareRideInteractor(storage=storage_mock)

        # Act
        interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_share_ride.assert_called_once_with(
            share_ride_dto=share_ride_dto)

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_true_and_create_share_ride(self,
                                                              storage_mock,
                                                              presenter_mock):
        # Arrange
        share_ride_dto = ShareRideDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=True,
            date_time=None,
            start_date_time="2020-07-22 01:00:00",
            end_date_time="2020-07-22 05:00:00"
        )
        interactor = ShareRideInteractor(storage=storage_mock)

        # Act
        interactor.create_share_ride_wrapper(
            share_ride_dto=share_ride_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_share_ride.assert_called_once_with(
            share_ride_dto=share_ride_dto)
