from lets_ride.models import RideRequest
from lets_ride.storages.ride_request_storage_implementation import \
    RideRequestStorageImplementation
import pytest
from freezegun import freeze_time

from lets_ride.tests.factories.interactor_dtos import RideRequestDtoFactory


class TestRideRequestStorageImplementation:
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
        no_of_seats = 2
        luggage_quantity = 0
        ride_request_dto = RideRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=False,
            date_time="2020-07-22 02:00:00",
            start_date_time=None,
            end_date_time=None,
            no_of_seats=2
        )
        print(ride_request_dto)
        storage = RideRequestStorageImplementation()

        # Act
        storage.create_ride_request(
            ride_request_dto=ride_request_dto
        )

        # Assert
        ride_request = RideRequest.objects.get(id=1)
        assert user_id == ride_request.id
        assert from_place == ride_request.from_place
        assert to_place == ride_request.to_place
        assert flexible_timings == ride_request.flexible_timings
        assert date_time == str(ride_request.date_time)
        assert start_date_time == ride_request.start_date_time
        assert end_date_time == ride_request.end_date_time
        assert no_of_seats == ride_request.no_of_seats
        assert luggage_quantity == ride_request.luggage_quantity

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
        no_of_seats = 2
        luggage_quantity = 1
        ride_request_dto = RideRequestDtoFactory(
            from_place="kurnool",
            to_place="hyd",
            flexible_timings=True,
            date_time=None,
            start_date_time="2020-07-22 02:00:00",
            end_date_time="2020-07-22 05:00:00",
            no_of_seats=2,
            luggage_quantity=1
        )
        print(ride_request_dto)
        storage = RideRequestStorageImplementation()

        # Act
        storage.create_ride_request(
            ride_request_dto=ride_request_dto
        )

        # Assert
        ride_request = RideRequest.objects.get(id=1)
        assert user_id == ride_request.id
        assert from_place == ride_request.from_place
        assert to_place == ride_request.to_place
        assert flexible_timings == ride_request.flexible_timings
        assert date_time == ride_request.date_time
        assert start_date_time == str(ride_request.start_date_time)
        assert end_date_time == str(ride_request.end_date_time)
        assert no_of_seats == ride_request.no_of_seats
        assert luggage_quantity == ride_request.luggage_quantity
