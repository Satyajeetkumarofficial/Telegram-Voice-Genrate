import os
import telebot
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

VOICE_IDS = {
    "hindi_male": "N2lVS1w4EtoT3dr4eOWO",
    "hindi_female": "5Q0t7uMcjvnagumL0L3b",
    "english_male": "pNInz6obpgDQGcFmaJgB",
    "english_female": "21m00Tcm4TlvDq8ikWAM"
}

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def generate_voice(text, voice_id, lang="hi"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    return "output.mp3"

@bot.message_handler(commands=['bol', 'speak'])
def handle_message(message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        bot.reply_to(message, "कृपया कुछ टेक्स्ट भेजें।")
        return
    content = text[1]
    if message.text.startswith("/bol"):
        voice_id = VOICE_IDS["hindi_male"]
    else:
        voice_id = VOICE_IDS["english_male"]
    file_path = generate_voice(content, voice_id)
    with open(file_path, "rb") as f:
        bot.send_voice(message.chat.id, f)

bot.polling()