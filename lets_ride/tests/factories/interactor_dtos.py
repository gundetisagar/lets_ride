import factory
import datetime

from lets_ride.dtos.dtos import RideRequestDTO


class RideRequestDtoFactory(factory.Factory):
    class Meta:
        model = RideRequestDTO

    user_id = 1
    from_place = factory.Sequence(lambda n: "form_place_%d" % n)
    to_place = factory.Sequence(lambda n: "to_place_%d" % n)
    datetime = None
    flexible_timings = False
    start_datetime = None
    end_datetime = None
    no_of_seats = 2
    luggage_quantity = 0

