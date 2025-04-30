import os
import telebot
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def generate_voice(text, lang="hi"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    return "output.mp3"

@bot.message_handler(commands=['bol', 'speak'])
def handle_message(message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        bot.reply_to(message, "कृपया कुछ टेक्स्ट भेजें।")
        return
    content = text[1]
    if message.text.startswith("/bol"):
        lang = "hi"
    else:
        lang = "en"
    file_path = generate_voice(content, lang)
    with open(file_path, "rb") as f:
        bot.send_voice(message.chat.id, f)

bot.polling()