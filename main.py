import os
import telebot
from gtts import gTTS
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def generate_voice(text, lang="hi"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    return "output.mp3"

def save_text_to_file(text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"text_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return filename

def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

@bot.message_handler(commands=['start'])
def handle_start(message):
    first_name = message.from_user.first_name or "User"
    greeting = get_greeting()
    welcome_text = f"{greeting}, {first_name}! Welcome to the Voice Bot. Use /bol, /speak or /txt to begin."
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['bol', 'speak'])
def handle_voice_commands(message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        bot.reply_to(message, "कृपया कुछ टेक्स्ट भेजें।")
        return
    content = text[1]
    lang = "hi" if message.text.startswith("/bol") else "en"
    file_path = generate_voice(content, lang)
    with open(file_path, "rb") as f:
        bot.send_voice(message.chat.id, f)

@bot.message_handler(commands=['txt'])
def handle_text_command(message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        bot.reply_to(message, "कृपया कुछ टेक्स्ट भेजें जिसे सेव किया जाए।")
        return
    content = text[1]
    filename = save_text_to_file(content)
    with open(filename, "rb") as f:
        bot.send_document(message.chat.id, f)

bot.polling()