from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# 建立 FastAPI 應用實例
app = FastAPI(
    title="FastAPI Demo",
    description="FastAPI 示範專案 - 測試端點",
    version="1.0.0"
)

# 定義請求模型
class TestRequest(BaseModel):
    key: str

# 測試用 GET 端點
@app.get("/api/test", 
         summary="測試 GET 端點",
         description="當訪問時會回傳 Hello World")
async def test_get():
    return {"message": "Hello World"}

# 測試用 POST 端點
@app.post("/api/test",
          summary="測試 POST 端點",
          description="當 key 等於 cxcxc 時回傳 Succeeded，否則回傳 Failed")
async def test_post(request: TestRequest):
    if request.key == "cxcxc":
        return {"status": "Succeeded"}
    return {"status": "Failed"}

# 根路徑
@app.get("/")
async def root():
    return {"message": "歡迎使用 FastAPI 測試服務"}

# 健康檢查端點
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    # 啟動服務
    uvicorn.run(app, host="0.0.0.0", port=8000)