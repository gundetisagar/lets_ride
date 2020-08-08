import enum

from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"


class AssetTypes(BaseEnumClass, enum.Enum):
    PARCEL = "PARCEL"
    BAG = "BAG"
    FURNITURE = "FURNITURE"
    OTHERS = "OTHERS"


class AssetSensitivityTypes(BaseEnumClass, enum.Enum):
    SENSITIVITY = "SENSITIVITY"
    HIGHLY_SENSITIVITY = "HIGHLY_SENSITIVITY"
    ELECTRONIC = "ELECTRONIC"


class TravelMediumTypes(BaseEnumClass, enum.Enum):
    CAR = "CAR"
    BUS = "BUS"
    FLIGHT = "FLIGHT"


class RideRequestStatusTypes(BaseEnumClass, enum.Enum):
    ALL = "ALL"
    PENDING = "PENDING"
    CONFIRM = "CONFIRM"
    EXPIRED = "EXPIRED"
