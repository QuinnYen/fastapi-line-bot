import json
import os
from typing import List
from ..models.user import User

class UserDao:
    def __init__(self):
        # 使用絕對路徑
        self.data_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "users.json")
        self._ensure_data_file()

    def _ensure_data_file(self):
        """確保資料檔案存在"""
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False)

    def get_all_users(self) -> List[User]:
        """列出所有用戶資料"""
        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [User(**user) for user in data]

    def add_user(self, user: User) -> bool:
        """新增用戶資料"""
        users = self.get_all_users()
        users.append(user)
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([user.dict() for user in users], f, ensure_ascii=False, indent=2)
        return True