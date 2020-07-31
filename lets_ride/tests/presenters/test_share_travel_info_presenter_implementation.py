from lets_ride.presenters.share_travel_info_presenter_implementation import \
    ShareTravelInfoPresenterImplementation
import json


def test_raise_exception_for_from_and_to_place_are_same(snapshot):
    # Arrange
    json_presenter = ShareTravelInfoPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_from_and_to_place_are_same()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_date_time(snapshot):
    # Arrange
    json_presenter = ShareTravelInfoPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_date_time()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_end_datetime(snapshot):
    # Arrange
    json_presenter = ShareTravelInfoPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_end_datetime()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_assets_quantity(snapshot):
    # Arrange
    json_presenter = ShareTravelInfoPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_assets_quantity()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")
