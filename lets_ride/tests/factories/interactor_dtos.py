import factory
import datetime

from lets_ride.dtos.dtos import RideRequestDTO


class RideRequestDtoFactory(factory.Factory):
    class Meta:
        model = RideRequestDTO

    user_id = 1
    from_place = factory.Sequence(lambda n: "form_place_%d" % n)
    to_place = factory.Sequence(lambda n: "to_place_%d" % n)
    date_time = "2020-07-22 01:00:00"
    flexible_timings = False
    start_date_time = None
    end_date_time = None
    no_of_seats = 2
    luggage_quantity = 0

