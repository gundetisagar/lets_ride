import factory
from lets_ride_auth.models.user import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username_%d" % n)
    name = factory.Sequence(lambda n: "name_%0d" % n)
    mobile_number = factory.Sequence(lambda n: "90000000%01d" % n)
