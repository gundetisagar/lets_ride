from lets_ride.models import AssetTransportRequest
from lets_ride.storages.asset_transport_request_storage_implementation import \
    AssetTransportRequestStorageImplementation
import pytest
from freezegun import freeze_time

from lets_ride.tests.factories.interactor_dtos import \
    AssetTransportRequestDtoFactory


class TestAssetTransportRequestStorageImplementation:

    @freeze_time("2020-07-22 00:00:00")
    @pytest.mark.django_db
    def test_with_flexible_timings_false_create(self):
        # Arrange
        user_id = 1
        from_place = "form_place_0"
        to_place = "to_place_0"
        flexible_timings = False
        date_time = "2020-07-22 02:00:00"
        start_date_time = None
        end_date_time = None
        no_of_assets = 2
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            flexible_timings=False,
            date_time="2020-07-22 02:00:00",
            start_date_time=None,
            end_date_time=None,
            no_of_assets=2
        )
        storage = AssetTransportRequestStorageImplementation()

        # Act
        storage.create_asset_transport_request(
            asset_transport_request_dto=asset_transport_request_dto
        )

        # Assert
        asset_request = AssetTransportRequest.objects.get(id=1)
        assert user_id == asset_request.id
        assert from_place == asset_request.from_place
        assert to_place == asset_request.to_place
        assert flexible_timings == asset_request.flexible_timings
        assert date_time == str(asset_request.date_time)
        assert start_date_time == asset_request.start_date_time
        assert end_date_time == asset_request.end_date_time
        assert no_of_assets == asset_request.no_of_assets


    @freeze_time("2020-07-22 00:00:00")
    @pytest.mark.django_db
    def test_with_flexible_timings_true_create(self):
        # Arrange
        user_id = 1
        from_place = "form_place_1"
        to_place = "to_place_1"
        flexible_timings = True
        date_time = None
        start_date_time = "2020-07-22 02:00:00"
        end_date_time = "2020-07-22 05:00:00"
        no_of_assets = 2
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            flexible_timings=True,
            date_time=None,
            start_date_time="2020-07-22 02:00:00",
            end_date_time="2020-07-22 05:00:00",
            no_of_assets=2
        )
        storage = AssetTransportRequestStorageImplementation()

        # Act
        storage.create_asset_transport_request(
            asset_transport_request_dto=asset_transport_request_dto
        )

        # Assert
        asset_request = AssetTransportRequest.objects.get(id=1)
        assert user_id == asset_request.id
        assert from_place == asset_request.from_place
        assert to_place == asset_request.to_place
        assert flexible_timings == asset_request.flexible_timings
        assert date_time == asset_request.date_time
        assert start_date_time == str(asset_request.start_date_time)
        assert end_date_time == str(asset_request.end_date_time)
        assert no_of_assets == asset_request.no_of_assets

    @freeze_time("2020-07-22 00:00:00")
    @pytest.mark.django_db
    def test_with_asset_type_others_and_create_asset_request(self):
        # Arrange
        user_id = 1
        from_place = "form_place_2"
        to_place = "to_place_2"
        flexible_timings = False
        date_time = "2020-07-22 01:00:00"
        start_date_time = None
        end_date_time = None
        no_of_assets = 1
        from lets_ride.constants.enums import AssetTypes
        asset_type = AssetTypes.OTHERS.value
        others = "mobile"
        whom_to_deliver = "sai-9876543210"
        asset_transport_request_dto = AssetTransportRequestDtoFactory(
            asset_type="OTHERS",
            others="mobile",
            asset_sensitivity="SENSITIVITY",
        )
        storage = AssetTransportRequestStorageImplementation()

        # Act
        storage.create_asset_transport_request(
            asset_transport_request_dto=asset_transport_request_dto
        )

        # Assert
        asset_request = AssetTransportRequest.objects.get(id=1)
        assert user_id == asset_request.id
        assert from_place == asset_request.from_place
        assert to_place == asset_request.to_place
        assert flexible_timings == asset_request.flexible_timings
        assert date_time == str(asset_request.date_time)
        assert start_date_time == asset_request.start_date_time
        assert end_date_time == asset_request.end_date_time
        assert no_of_assets == asset_request.no_of_assets
        assert asset_type == asset_request.asset_type
        assert others == asset_request.others
        assert whom_to_deliver == asset_request.whom_to_deliver
