# Telegram Voice Bot using ElevenLabs

## Features
- Hindi, Hinglish, English text-to-speech
- Male/Female high-quality voices
- Uses ElevenLabs API
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

3. Add your Telegram bot token and ElevenLabs API key in `.env`

## Run Locally
```
python main.py
```

## Deploy to Koyeb
- Create a GitHub repo and push files
- Go to [https://app.koyeb.com/](https://app.koyeb.com/)
- Create service from GitHub
- Add environment variables: TELEGRAM_TOKEN and ELEVENLABS_API_KEY
- Done!