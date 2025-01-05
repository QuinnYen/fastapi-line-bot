from fastapi import APIRouter, HTTPException
from typing import List
from ..models.user import User
from ..services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/api/user", response_model=List[User])
async def get_users():
    """獲取所有用戶資料"""
    try:
        return user_service.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/user")
async def create_user(user: User):
    """新增用戶資料"""
    try:
        success = user_service.add_user(user)
        if success:
            return {"message": "用戶資料新增成功"}
        else:
            raise HTTPException(status_code=400, detail="用戶資料新增失敗")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))