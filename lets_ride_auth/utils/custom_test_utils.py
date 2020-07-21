from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time
from lets_ride_auth.models.user import User
import factory


class CustomTestUtils(CustomAPITestCase):

    def create_users(self):
        pass


# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User

#     username = "username"
#     password = "password"