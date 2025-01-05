# 使用 Python 3.9 slim 版本作為基礎映像
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製專案檔案
COPY requirements.txt .
COPY .env .
COPY app/ ./app/

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 設定環境變數
ENV PYTHONPATH=/app

# 暴露端口
EXPOSE 8000

# 啟動命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]