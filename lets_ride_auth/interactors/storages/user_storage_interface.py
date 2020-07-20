import abc


class UserStorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_username(self, username: str) -> bool:
        pass

    @abc.abstractmethod
    def validate_password(self, username: str, password: str) -> int:
        pass

    #
    # @abc.abstractmethod
    # def get_user_profile(self, user_id: int) -> UserDetailsDto:
    #     pass

    @abc.abstractmethod
    def validate_user_id(self, user_id: int) -> bool:
        pass
