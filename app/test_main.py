from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TestInput(BaseModel):
    key: str

@app.get("/api/test")
async def test_get():
    """GET測試端點"""
    return "Hello World"

@app.post("/api/test")
async def test_post(data: TestInput):
    """POST測試端點"""
    if data.key == "cxcxc":
        return "Succeeded"
    return "Failed"

# 如果是直接執行此檔案，啟動伺服器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)