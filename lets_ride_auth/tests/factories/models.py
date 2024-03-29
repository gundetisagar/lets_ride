import factory
from lets_ride_auth.models.user import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n + 1}")
    name = factory.Sequence(lambda n: f"name_{n + 1}")
    mobile_number = factory.Sequence(lambda n: f"987654321{n}")
