from fastapi import APIRouter, Request, HTTPException
from linebot.exceptions import InvalidSignatureError
from ..services.line_service import LineService
import os
import traceback
import logging

# 設定日誌
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()

# 從環境變數獲取設定
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 檢查環境變數
logger.debug(f"LINE_CHANNEL_ACCESS_TOKEN: {LINE_CHANNEL_ACCESS_TOKEN}")
logger.debug(f"LINE_CHANNEL_SECRET: {LINE_CHANNEL_SECRET}")
logger.debug(f"GEMINI_API_KEY: {GEMINI_API_KEY}")

if not all([LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET, GEMINI_API_KEY]):
    logger.error("缺少必要的環境變數")

line_service = LineService(
    channel_access_token=LINE_CHANNEL_ACCESS_TOKEN,
    channel_secret=LINE_CHANNEL_SECRET,
    gemini_api_key=GEMINI_API_KEY
)

@router.post("/api/llm")
async def line_webhook(request: Request):
    """LINE Webhook"""
    try:
        logger.debug("收到 webhook 請求")
        signature = request.headers.get("X-Line-Signature", "")
        logger.debug(f"Signature: {signature}")
        
        body = await request.body()
        body_text = body.decode()
        logger.debug(f"Request body: {body_text}")
        
        await line_service.handler.handle(body_text, signature)
        return {"message": "OK"}
        
    except InvalidSignatureError as e:
        logger.error(f"簽名驗證失敗: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=400, detail="Invalid signature")
        
    except Exception as e:
        logger.error(f"處理 webhook 時發生錯誤: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))