from typing import List


class UserService:
	@property
	def interface(self):
		from lets_ride_auth.interfaces.user_interface import UserInterface
		return UserInterface()

    def get_users_profile_dtos(self, user_ids: List[int]):
        user_profile_dtos = self.interface.get_users_profile_dtos(user_ids=user_ids)
        return user_profile_dtos
