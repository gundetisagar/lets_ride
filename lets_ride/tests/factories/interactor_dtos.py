import datetime

import factory
from lets_ride.constants.enums import AssetTypes, AssetSensitivityTypes, \
    TravelMediumTypes
from lets_ride.dtos.dtos import RideRequestDTO, ShareRideDTO, \
    AssetTransportRequestDTO, ShareTravelInfoDTO


class RideRequestDtoFactory(factory.Factory):
    class Meta:
        model = RideRequestDTO

    user_id = 1
    from_place = factory.Sequence(lambda n: "form_place_%d" % n)
    to_place = factory.Sequence(lambda n: "to_place_%d" % n)
    date_time = datetime.datetime(2020, 7, 22, 1, 00, 00)
    flexible_timings = False
    start_date_time = None
    end_date_time = None
    no_of_seats = 2
    luggage_quantity = 0


class ShareRideDtoFactory(factory.Factory):
    class Meta:
        model = ShareRideDTO

    user_id = 1
    from_place = factory.Sequence(lambda n: "form_place_%d" % n)
    to_place = factory.Sequence(lambda n: "to_place_%d" % n)
    date_time = datetime.datetime(2020, 7, 22, 1, 00, 00)
    flexible_timings = False
    start_date_time = None
    end_date_time = None
    no_of_seats_available = 2
    assets_quantity = 0


class AssetTransportRequestDtoFactory(factory.Factory):
    class Meta:
        model = AssetTransportRequestDTO

    user_id = 1
    from_place = factory.Sequence(lambda n: "form_place_%d" % n)
    to_place = factory.Sequence(lambda n: "to_place_%d" % n)
    date_time = datetime.datetime(2020, 7, 22, 1, 00, 00)
    flexible_timings = False
    start_date_time = None
    end_date_time = None
    no_of_assets = 1
    asset_type = AssetTypes.PARCEL.value
    others = None
    asset_sensitivity = AssetSensitivityTypes.ELECTRONIC.value
    whom_to_deliver = "sai-9876543210"


class ShareTravelInfoDtoFactory(factory.Factory):
    class Meta:
        model = ShareTravelInfoDTO

    user_id = 1
    from_place = factory.Sequence(lambda n: "form_place_%d" % n)
    to_place = factory.Sequence(lambda n: "to_place_%d" % n)
    date_time = datetime.datetime(2020, 7, 22, 1, 00, 00)
    flexible_timings = False
    start_date_time = None
    end_date_time = None
    travel_medium = TravelMediumTypes.CAR.value
    assets_quantity = 1
