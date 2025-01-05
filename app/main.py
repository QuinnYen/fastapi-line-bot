from fastapi import FastAPI
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

from .controllers.user_controller import router as user_router
from .controllers.line_controller import router as line_router

app = FastAPI(
    title="用戶管理系統",
    description="FastAPI MVC 示範專案",
    version="1.0.0"
)

# 註冊路由
app.include_router(user_router)
app.include_router(line_router)

@app.get("/")
async def root():
    return {"message": "歡迎使用用戶管理系統"}