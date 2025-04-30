# Telegram Voice Bot using gTTS (Google Text-to-Speech)

## Features
- Hindi and English text-to-speech
- Free, no premium required
- Uses gTTS API
- Deployable to Koyeb

## Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Create `.env` file:
```
cp .env.example .env
```

3. Add your Telegram bot token in `.env`

## Run Locally
```
python main.py
```

## Deploy to Koyeb
- Create a GitHub repo and push files
- Go to [https://app.koyeb.com/](https://app.koyeb.com/)
- Create service from GitHub
- Add environment variables: TELEGRAM_TOKEN
- Done!