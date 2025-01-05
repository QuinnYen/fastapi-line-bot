from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
from .gemini_service import GeminiService
from .user_service import UserService
from ..models.user import User
import logging

logger = logging.getLogger(__name__)

class LineService:
    def __init__(self, channel_access_token: str, channel_secret: str, gemini_api_key: str):
        self.line_bot_api = LineBotApi(channel_access_token)
        self.handler = WebhookHandler(channel_secret)
        self.gemini_service = GeminiService(gemini_api_key)
        self.user_service = UserService()
        self._setup_handlers()

    def _setup_handlers(self):
        @self.handler.add(MessageEvent, message=TextMessage)
        def handle_message(event):
            """處理收到的訊息"""
            try:
                logger.debug(f"接收到訊息: {event.message.text}")
                
                # 使用 Gemini 解析訊息
                user_info = self.gemini_service.parse_user_info(event.message.text)
                logger.debug(f"Gemini 解析結果: {user_info}")
                
                if user_info and all(user_info.values()):
                    # 如果成功解析到完整的用戶資訊
                    user = User(**user_info)
                    success = self.user_service.add_user(user)
                    
                    if success:
                        response = f"已成功記錄用戶資訊：\n姓名：{user.name}\n身高：{user.height}cm\n體重：{user.weight}kg"
                    else:
                        response = "資料儲存失敗，請稍後再試。"
                else:
                    response = "無法從訊息中提取完整的用戶資訊，請確保包含姓名、身高和體重。"
                
                self.line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=response)
                )

            except Exception as e:
                logger.error(f"處理訊息時發生錯誤: {str(e)}", exc_info=True)
                self.line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="處理訊息時發生錯誤，請稍後再試。")
                )