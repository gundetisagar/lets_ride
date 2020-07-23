from django.db import models


class RideRequest(models.Model):
    user_id = models.IntegerField()
    from_place = models.CharField(max_length=50)
    to_place = models.CharField(max_length=50)
    flexible_timings = models.BooleanField(default=False)
    date_time = models.DateTimeField(null=True)
    start_date_time = models.DateTimeField(null=True)
    end_date_time = models.DateTimeField(null=True)
    no_of_seats = models.IntegerField()
    luggage_quantity = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add=True)
