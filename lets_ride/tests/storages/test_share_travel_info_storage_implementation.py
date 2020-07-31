from lets_ride.constants.enums import TravelMediumTypes
from lets_ride.models import ShareTravelInfo
from lets_ride.storages.share_travel_info_storage_implementation import \
    ShareTravelInfoStorageImplementation
import pytest
from freezegun import freeze_time

from lets_ride.tests.factories.interactor_dtos import ShareRideDtoFactory, \
    ShareTravelInfoDtoFactory


class TestShareTravelInfoStorageImplementation:
    @freeze_time("2020-07-22 00:00:00")
    @pytest.mark.django_db
    def test_with_flexible_timings_false_create(self):
        # Arrange
        user_id = 1
        from_place = "form_place_0"
        to_place = "to_place_0"
        flexible_timings = False
        date_time = "2020-07-22 01:00:00"
        start_date_time = None
        end_date_time = None
        assets_quantity = 1
        share_travel_info_dto = ShareTravelInfoDtoFactory()
        storage = ShareTravelInfoStorageImplementation()

        # Act
        storage.create_share_travel_info(
            share_travel_info_dto=share_travel_info_dto
        )

        # Assert
        share_travel_info_obj = ShareTravelInfo.objects.get(id=1)
        assert user_id == share_travel_info_obj.id
        assert from_place == share_travel_info_obj.from_place
        assert to_place == share_travel_info_obj.to_place
        assert flexible_timings == share_travel_info_obj.flexible_timings
        assert date_time == str(share_travel_info_obj.date_time)
        assert start_date_time == share_travel_info_obj.start_date_time
        assert end_date_time == share_travel_info_obj.end_date_time
        assert assets_quantity == share_travel_info_obj.assets_quantity

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
        assets_quantity = 1
        share_travel_info_dto = ShareTravelInfoDtoFactory(
            flexible_timings=True,
            date_time=None,
            start_date_time="2020-07-22 02:00:00",
            end_date_time="2020-07-22 05:00:00",
        )
        storage = ShareTravelInfoStorageImplementation()

        # Act
        storage.create_share_travel_info(
            share_travel_info_dto=share_travel_info_dto
        )

        # Assert
        share_travel_info_obj = ShareTravelInfo.objects.get(id=1)
        assert user_id == share_travel_info_obj.id
        assert from_place == share_travel_info_obj.from_place
        assert to_place == share_travel_info_obj.to_place
        assert flexible_timings == share_travel_info_obj.flexible_timings
        assert date_time == share_travel_info_obj.date_time
        assert start_date_time == str(share_travel_info_obj.start_date_time)
        assert end_date_time == str(share_travel_info_obj.end_date_time)
        assert assets_quantity == share_travel_info_obj.assets_quantity
