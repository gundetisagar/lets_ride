import datetime

from lets_ride.constants.enums import RideRequestStatusTypes
from lets_ride.dtos.dtos import RideRequestDTO
import factory

from lets_ride.interactors.dtos import MyRideRequestDTO, \
    MyRideRequestWithUserProfileDTO
from lets_ride.tests.factories.interactor_dtos import UserProfileDtoFactory


class MyRideRequestDtoFactory(factory.Factory):
    class Meta:
        model = MyRideRequestDTO

    user_id = 1
    from_place = factory.Sequence(lambda n: "form_place_%d" % n)
    to_place = factory.Sequence(lambda n: "to_place_%d" % n)
    date_time = datetime.datetime(2020, 7, 22, 1, 00, 00)
    flexible_timings = False
    start_date_time = None
    end_date_time = None
    no_of_seats = 2
    luggage_quantity = 0
    accepted_person = 2
    status = RideRequestStatusTypes.PENDING.value
#
# def my_ride_requests(size: int):
#     return MyRideRequestDtoFactory(size)

class MyRideRequestWithUserProfileDtoFactory(factory.Factory):
    class Meta:
        model = MyRideRequestWithUserProfileDTO

    ride_request_dtos = factory.SubFactory(MyRideRequestDtoFactory)
    user_profile_dtos = factory.SubFactory(UserProfileDtoFactory)
