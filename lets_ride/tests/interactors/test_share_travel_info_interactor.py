from unittest.mock import Mock
from datetime import datetime
import pytest
from freezegun import freeze_time

from lets_ride.constants.constants import DEFAULT_DATE_TIME_FORMAT
from lets_ride.interactors.share_travel_info_interactor import \
    ShareTravelInfoInteractor
from lets_ride.tests.factories.interactor_dtos import ShareTravelInfoDtoFactory


class TestShareTravelInfo:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from lets_ride.interactors.storages.share_travel_info_storage_interface \
            import ShareTravelInfoStorageInterface
        storage = create_autospec(ShareTravelInfoStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from lets_ride.interactors.presenters.share_travel_info_presenter_interface \
            import ShareTravelInfoPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(ShareTravelInfoPresenterInterface)
        return presenter

    @freeze_time("2020-07-22 00:00:00")
    def test_with_from_and_to_places_same_raises_exception(self,
                                                           storage_mock,
                                                           presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(from_place="kurnool",
                                                          to_place="kurnool")
        interactor = ShareTravelInfoInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_from_and_to_place_are_same. \
            return_value = mock_object

        # Act
        response = interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_from_and_to_place_are_same. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_with_from_and_to_places_with_different_places(self,
                                                           storage_mock,
                                                           presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            date_time=datetime.strptime("2020-07-22 11:00:00",
                                        DEFAULT_DATE_TIME_FORMAT)
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)

        # Act
        response = interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )
        # Assert
        presenter_mock.raise_exception_for_from_and_to_place_are_same. \
            assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_date_time_is_in_past_raise_exception(self, storage_mock,
                                                  presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            flexible_timings=False,
            date_time=datetime.strptime("2020-07-21 11:00:00",
                                        DEFAULT_DATE_TIME_FORMAT)
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_date_time. \
            return_value = mock_object

        # Act
        response = interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )
        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_date_time. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_given_date_time_is_greater_than_current_datetime_did_not_raise_exception(
            self, storage_mock,
            presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            flexible_timings=False,
            date_time=datetime.strptime("2020-07-22 01:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)

        # Act
        interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )
        presenter_mock.raise_exception_for_invalid_date_time.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_end_datetime_is_less_than_start_datetime_raises_exception(self,
                                                                       storage_mock,
                                                                       presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            flexible_timings=True,
            start_date_time=datetime.strptime("2020-07-22 12:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
            end_date_time=datetime.strptime("2020-07-22 11:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
        )

        interactor = ShareTravelInfoInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_end_datetime. \
            return_value = mock_object

        # Act
        response = interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_end_datetime. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_start_datetime_less_than_end_datetime_did_not_raises_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            flexible_timings=True,
            start_date_time=datetime.strptime("2020-07-22 12:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
            end_date_time=datetime.strptime("2020-07-22 13:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)

        # Act
        response = interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_end_datetime. \
            assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_assets_quantity_is_negative_raise_exception(self, storage_mock,
                                                         presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            assets_quantity=-1
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_assets_quantity. \
            return_value = mock_object
        # Act
        response = interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_assets_quantity. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_assets_quantity_is_zero_did_not_raise_exception(self,
                                                             storage_mock,
                                                             presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            assets_quantity=0
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)

        # Act
        interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_assets_quantity. \
            assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_false_and_create_share_ride(self,
                                                               storage_mock,
                                                               presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=False,
            date_time=datetime.strptime("2020-07-22 05:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)

        # Act
        interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_share_travel_info.assert_called_once_with(
            share_travel_info_dto=share_travel_info_dto)

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_true_and_create_share_ride(self,
                                                              storage_mock,
                                                              presenter_mock):
        # Arrange
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=True,
            date_time=None,
            start_date_time=datetime.strptime("2020-07-22 01:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
            end_date_time=datetime.strptime("2020-07-22 05:00:00",
                                        DEFAULT_DATE_TIME_FORMAT),
        )
        interactor = ShareTravelInfoInteractor(storage=storage_mock)

        # Act
        interactor.create_share_travel_info_wrapper(
            share_travel_info_dto=share_travel_info_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_share_travel_info.assert_called_once_with(
            share_travel_info_dto=share_travel_info_dto)
