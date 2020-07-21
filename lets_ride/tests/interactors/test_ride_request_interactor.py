from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.interactors.storages.ride_request_storage_interface import RideRequestInterface


class TestRideRequest:
    import pytest

    @pytest.fixture
    def ride_request_storage_mock(self):
        from fb_post_clean_arch_v2.interactors.storage_interfaces. \
            comment_storage_interface import StorageInterface
        from mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def ride_request_presenter_mock(self):
        from fb_post_clean_arch_v2.interactors.presenter_interfaces. \
            presenter_interface import CreateReplyPresenterInterface
        from mock import create_autospec
        presenter = create_autospec(CreateReplyPresenterInterface)
        return presenter

    def test_ride_requset_with_from_and_to_locations(self, ride_request_storage_mock,
                                                      ride_request_presenter_mock):
        # Arrange


        # Act

        # Assert