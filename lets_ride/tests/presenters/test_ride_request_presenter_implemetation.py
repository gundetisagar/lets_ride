from lets_ride.presenters.ride_request_presenter_implementation import RideRequestPresenterImplementation
import json


def test_raise_exception_for_from_and_to_place_are_same(snapshot):
    # Arrange
    json_presenter = RideRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_from_and_to_place_are_same()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_date_time(snapshot):
    # Arrange
    json_presenter = RideRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_date_time()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_end_datetime(snapshot):
    # Arrange
    json_presenter = RideRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_end_datetime()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")


def test_raise_exception_for_invalid_no_of_seats(snapshot):
    # Arrange
    json_presenter = RideRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_no_of_seats()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")

def test_raise_exception_for_invalid_luggage_quantity(snapshot):
    # Arrange
    json_presenter = RideRequestPresenterImplementation()
    # Act
    response_object = json_presenter.raise_exception_for_invalid_luggage_quantity()
    # Assert
    response = json.loads(response_object.content)
    snapshot.assert_match(response, "response")
