import factory
from lets_ride_auth.models.user import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "user_1"
    mobile_number = "9876543210"
    password = "user@1234"

    # username = factory.Sequence(lambda n: "username_{0}".format(n + 1))
    # name = factory.Sequence(lambda n: "name_{0}".format(n + 1))
    # mobile_number = factory.Sequence(lambda n: "90000000%01d" % n)
