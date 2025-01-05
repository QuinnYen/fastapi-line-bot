import google.generativeai as genai
from typing import Dict, Optional
import json

class GeminiService:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def parse_user_info(self, text: str) -> Optional[Dict]:
        """解析文本中的用戶資訊"""
        prompt = f"""
        請從以下文本中提取用戶的姓名、身高和體重資訊，並以JSON格式回傳。
        如果無法提取完整資訊，對應欄位請回傳null。
        
        文本: {text}
        
        請以下列JSON格式回傳:
        {{
            "name": "姓名",
            "height": 數值,
            "weight": 數值
        }}
        """
        
        try:
            # 使用同步方式生成內容
            response = self.model.generate_content(prompt)
            response_text = response.text
            
            # 找出JSON部分
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start >= 0 and end > start:
                json_str = response_text[start:end]
                return json.loads(json_str)
            return None
        except Exception as e:
            print(f"Error parsing with Gemini: {e}")
            return None