from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    mobile_number = models.CharField(max_length=10)
    profile_pic = models.CharField(max_length=200, default="profile_pic_url")

    def __str__(self):
        return "{}".format(self.username)
