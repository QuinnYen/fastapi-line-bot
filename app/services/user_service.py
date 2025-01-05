from typing import List
from ..models.user import User
from ..dao.user_dao import UserDao

class UserService:
    def __init__(self):
        self.user_dao = UserDao()

    def get_all_users(self) -> List[User]:
        """獲取所有用戶"""
        return self.user_dao.get_all_users()

    def add_user(self, user: User) -> bool:
        """新增用戶"""
        return self.user_dao.add_user(user)