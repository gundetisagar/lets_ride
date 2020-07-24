from django.db import models

from lets_ride.constants.enums import AssetTypes, AssetSensitivityTypes


class AssetTransportRequest(models.Model):
    user_id = models.IntegerField()
    from_place = models.CharField(max_length=50)
    to_place = models.CharField(max_length=50)
    flexible_timings = models.BooleanField(default=False)
    date_time = models.DateTimeField(null=True)
    start_date_time = models.DateTimeField(null=True)
    end_date_time = models.DateTimeField(null=True)
    no_of_assets = models.IntegerField()
    asset_type = models.CharField(max_length=20,
                                  choices=AssetTypes.get_list_of_tuples())
    others = models.CharField(max_length=50, null=True)
    asset_sensitivity = models.CharField(
        max_length=20, choices=AssetSensitivityTypes.get_list_of_tuples())
    whom_to_deliver = models.CharField(max_length=100)
