import factory

from lets_ride_auth.dtos.dtos import UserProfileDTO


class UserProfileDtoFactory(factory.Factory):
    class Meta:
        model = UserProfileDTO

    user_id = factory.Sequence(lambda n: n + 1)
    username = factory.Sequence(lambda n: f"user_{n + 1}")
    name = factory.Sequence(lambda n: f"name_{n + 1}")
    mobile_number = factory.Sequence(lambda n: f"987654321{n}")
