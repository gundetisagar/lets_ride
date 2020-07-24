from lets_ride.presenters.asset_transport_request_presenter_implementation\
    import AssetTransportRequestPresenterImplementation
import json


def test_raise_exception_for_from_and_to_place_are_same(snapshot):
    # Arrange
    json_presenter = AssetTransportRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_from_and_to_place_are_same()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_date_time(snapshot):
    # Arrange
    json_presenter = AssetTransportRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_date_time()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_end_datetime(snapshot):
    # Arrange
    json_presenter = AssetTransportRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_end_datetime()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_no_of_assets(snapshot):
    # Arrange
    json_presenter = AssetTransportRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_no_of_assets()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")

def test_raise_exception_for_invalid_whom_to_deliver(snapshot):
    # Arrange
    json_presenter = AssetTransportRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_whom_to_deliver()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")
