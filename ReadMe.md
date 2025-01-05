# FastAPI Line Bot

這是一個使用 FastAPI 框架開發的 LINE Bot 專案，整合了 Google Gemini 進行自然語言處理。

## 功能特點

- 使用 FastAPI 建立 Web API
- 整合 LINE Messaging API
- 使用 Google Gemini 進行文本分析
- Docker 容器化部署
- MVC 架構設計

## 專案結構

```
fastapi-line-bot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── dao/
│   │   ├── __init__.py
│   │   └── user_dao.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── line_service.py
│   │   └── gemini_service.py
│   └── controllers/
│       ├── __init__.py
│       └── user_controller.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## 前置需求

- Python 3.9+
- Docker Desktop
- ngrok
- LINE Developers 帳號
- Google Gemini API 金鑰

## 環境設定

1. 複製專案後，建立 `.env` 檔案，填入以下資訊：
```ini
LINE_CHANNEL_ACCESS_TOKEN=你的LINE Channel Access Token
LINE_CHANNEL_SECRET=你的LINE Channel Secret
GEMINI_API_KEY=你的Gemini API Key
```

2. 安裝 Docker Desktop
   - 從 [Docker 官網](https://docs.docker.com/desktop/install/windows-install/) 下載並安裝

3. 安裝 ngrok
   - 下載 ngrok
   - 設定 authtoken：`ngrok config add-authtoken 你的authtoken`

## 部署步驟

1. 建立 Docker 映像檔：
```bash
docker build -t fastapi-line-bot .
```

2. 運行容器：
```bash
docker run -d -p 8000:8000 --name line-bot --env-file .env fastapi-line-bot
```

3. 啟動 ngrok：
```bash
ngrok http 8000
```

4. 設定 LINE Bot Webhook：
   - 複製 ngrok 產生的 HTTPS URL
   - 在 LINE Developers Console 中設定 Webhook URL
   - URL 格式：`https://你的ngrok網址/api/llm`
   - 開啟 "Use webhook" 選項
   - 測試連線

## 使用方法

1. 加入你的 LINE Bot 為好友

2. 發送包含姓名、身高和體重的訊息，例如：
```
小明 身高180公分 體重70公斤
```

3. Bot 會回覆已記錄的資訊

## 常見問題排解

1. 如果 LINE Bot 沒有回應：
   - 確認 Docker 容器是否正常運行
   - 檢查 ngrok 是否正常轉發
   - 確認 Webhook URL 是否正確設定
   - 檢查環境變數是否正確

2. 檢查容器日誌：
```bash
docker logs line-bot -f
```

## 注意事項

- ngrok 每次重新啟動都會產生新的 URL，需要更新 LINE Bot 的 Webhook URL
- 確保 .env 檔案中的金鑰資訊不要外洩
- 本地開發時需要確保 8000 端口未被占用