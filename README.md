# Telegram Hello Bot

Bot Telegram tối giản để test server.

## Tính năng

- Gửi `/start` → bot trả lời `Hello 👋`
- `GET /` → kiểm tra ứng dụng đang chạy
- `GET /health` → endpoint dành cho UptimeRobot

## Chạy local

```bash
pip install -r requirements.txt
```

Tạo biến môi trường:

```bash
BOT_TOKEN=YOUR_BOT_TOKEN
```

Sau đó:

```bash
python bot.py
```

## Deploy

Trên dịch vụ host Python, cấu hình biến môi trường:

```
BOT_TOKEN=token_lay_tu_BotFather
```

Start command:

```
gunicorn --workers 1 --threads 4 --bind 0.0.0.0:$PORT bot:app
```

Sau khi deploy, dùng URL sau cho UptimeRobot:

```
https://YOUR-SERVICE-URL/health
```

> Không commit Telegram token vào GitHub.
