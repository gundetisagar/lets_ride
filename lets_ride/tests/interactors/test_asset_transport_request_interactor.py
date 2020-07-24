import pytest
from freezegun import freeze_time
from unittest.mock import patch, Mock

from lets_ride.tests.factories.interactor_dtos import \
    AssetTransportRequestDtoFactory
from lets_ride.interactors.mixins.Validations import ValidationMixin
from lets_ride.interactors.asset_transport_request_inreractor import \
    AssetTransportRequestInteractor


class TestAssetTransportRequest:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from lets_ride.interactors.storages. \
            asset_transport_request_storage_interface import \
            AssetTransportRequestStorageInterface
        storage = create_autospec(AssetTransportRequestStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from lets_ride.interactors.presenters.asset_transport_request_presenter_interface \
            import AssetTransportRequestPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(AssetTransportRequestPresenterInterface)
        return presenter

    @freeze_time("2020-07-22 00:00:00")
    def test_with_from_and_to_places_same_raises_exception(self,
                                                           storage_mock,
                                                           presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            from_place="kurnool",
            to_place="kurnool")
        interactor = AssetTransportRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_from_and_to_place_are_same. \
            return_value = mock_object

        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
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
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            date_time="2020-07-22 11:00:00"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )
        # Assert
        presenter_mock.raise_exception_for_from_and_to_place_are_same. \
            assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_date_time_is_in_past_raise_exception(self, storage_mock,
                                                  presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            flexible_timings=False,
            date_time="2020-07-21 11:00:00"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_date_time.return_value = mock_object

        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
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
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            flexible_timings=False,
            date_time="2020-07-22 01:00:00"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )
        presenter_mock.raise_exception_for_invalid_date_time.assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_end_datetime_is_less_than_start_datetime_raises_exception(self,
                                                                       storage_mock,
                                                                       presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            flexible_timings=True,
            start_date_time="2020-07-22 12:00:00",
            end_date_time="2020-07-22 11:00:00"
        )

        interactor = AssetTransportRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_end_datetime.return_value = mock_object

        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
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
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            flexible_timings=True,
            start_date_time="2020-07-22 12:00:00",
            end_date_time="2020-07-22 13:00:00"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_end_datetime. \
            assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_assets_equals_to_zero_raise_exception(self, storage_mock,
                                                         presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            no_of_assets=0
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_no_of_assets.return_value = mock_object
        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_no_of_assets. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_assets_is_negative_raise_exception(self, storage_mock,
                                                      presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            no_of_assets=-1
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_no_of_assets. \
            return_value = mock_object
        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_no_of_assets. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_no_of_assets_is_positive_did_not_raise_exception(self,
                                                              storage_mock,
                                                              presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            no_of_assets=1
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_no_of_assets. \
            assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_whom_to_deliver_with_less_than_12_chars_raise_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            whom_to_deliver="12345678911"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_whom_to_deliver. \
            return_value = mock_object
        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_whom_to_deliver. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_whom_to_deliver_with_equals_to_12_chars_raise_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            whom_to_deliver="123456789012"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)
        mock_object = Mock()
        presenter_mock.raise_exception_for_invalid_whom_to_deliver. \
            return_value = mock_object
        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_whom_to_deliver. \
            assert_called_once()

    @freeze_time("2020-07-22 00:00:00")
    def test_whom_to_deliver_with_greater_than_12_chars_did_not_raise_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            whom_to_deliver="1234567890013"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        response = interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_whom_to_deliver. \
            assert_not_called()

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_false_and_create_ride_request(self,
                                                                 storage_mock,
                                                                 presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=False,
            date_time="2020-07-22 05:00:00",

        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_asset_transport_request.assert_called_once_with(
            asset_transport_request_dto=asset_transport_request_dto)

    @freeze_time("2020-07-22 00:00:00")
    def test_with_flexible_timings_true_and_create_ride_request(self,
                                                                storage_mock,
                                                                presenter_mock):
        # Arrange
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=True,
            date_time=None,
            start_date_time="2020-07-22 01:00:00",
            end_date_time="2020-07-22 05:00:00"
        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_asset_transport_request.assert_called_once_with(
            asset_transport_request_dto=asset_transport_request_dto)

    @freeze_time("2020-07-22 00:00:00")
    def test_with_assey_type_other_and_create_ride_request(self,
                                                                storage_mock,
                                                                presenter_mock):
        # Arrange
        from lets_ride.constants.enums import AssetTypes
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            asset_type=AssetTypes.PARCEL.value,
            others="Books"

        )
        interactor = AssetTransportRequestInteractor(storage=storage_mock)

        # Act
        interactor.create_asset_transport_request_wrapper(
            asset_transport_request_dto=asset_transport_request_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.create_asset_transport_request.assert_called_once_with(
            asset_transport_request_dto=asset_transport_request_dto)