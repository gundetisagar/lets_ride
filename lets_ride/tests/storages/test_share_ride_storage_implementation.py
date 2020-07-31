from lets_ride.models import ShareRide
from lets_ride.storages.share_ride_storage_implementation import \
    ShareRideStorageImplementation
import pytest
from freezegun import freeze_time

from lets_ride.tests.factories.interactor_dtos import ShareRideDtoFactory


class TestShareRideStorageImplementation:
    @freeze_time("2020-07-22 00:00:00")
    @pytest.mark.django_db
    def test_with_flexible_timings_false_create(self):
        # Arrange
        user_id = 1
        from_place = "kurnool"
        to_place = "hyd"
        flexible_timings = False
        date_time = "2020-07-22 02:00:00"
        start_date_time = None
        end_date_time = None
        no_of_seats_available = 2
        assets_quantity = 0
        share_ride_dto = ShareRideDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=False,
            date_time="2020-07-22 02:00:00",
            start_date_time=None,
            end_date_time=None,
            no_of_seats_available=2
        )
        storage = ShareRideStorageImplementation()

        # Act
        storage.create_share_ride(
            share_ride_dto=share_ride_dto
        )

        # Assert
        share_ride_obj = ShareRide.objects.get(id=1)
        assert user_id == share_ride_obj.id
        assert from_place == share_ride_obj.from_place
        assert to_place == share_ride_obj.to_place
        assert flexible_timings == share_ride_obj.flexible_timings
        assert date_time == str(share_ride_obj.date_time)
        assert start_date_time == share_ride_obj.start_date_time
        assert end_date_time == share_ride_obj.end_date_time
        assert no_of_seats_available == share_ride_obj.no_of_seats_available
        assert assets_quantity == share_ride_obj.assets_quantity

    @freeze_time("2020-07-22 00:00:00")
    @pytest.mark.django_db
    def test_with_flexible_timings_true_create(self):
        # Arrange
        user_id = 1
        from_place = "kurnool"
        to_place = "hyd"
        flexible_timings = True
        date_time = None
        start_date_time = "2020-07-22 02:00:00"
        end_date_time = "2020-07-22 05:00:00"
        no_of_seats_available = 2
        assets_quantity = 1
        share_ride_dto = ShareRideDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=True,
            date_time=None,
            start_date_time="2020-07-22 02:00:00",
            end_date_time="2020-07-22 05:00:00",
            no_of_seats_available=2,
            assets_quantity=1
        )
        storage = ShareRideStorageImplementation()

        # Act
        storage.create_share_ride(
            share_ride_dto=share_ride_dto
        )

        # Assert
        share_ride_obj = ShareRide.objects.get(id=1)
        assert user_id == share_ride_obj.id
        assert from_place == share_ride_obj.from_place
        assert to_place == share_ride_obj.to_place
        assert flexible_timings == share_ride_obj.flexible_timings
        assert date_time == share_ride_obj.date_time
        assert start_date_time == str(share_ride_obj.start_date_time)
        assert end_date_time == str(share_ride_obj.end_date_time)
        assert no_of_seats_available == share_ride_obj.no_of_seats_available
        assert assets_quantity == share_ride_obj.assets_quantity
