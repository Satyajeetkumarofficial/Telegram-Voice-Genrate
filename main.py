import os
import telebot
from gtts import gTTS
from datetime import datetime
from dotenv import load_dotenv
from threading import Thread
from flask import Flask, request
import telebot

API_TOKEN = '7034110540:AAEX1L-VZgRb_utswsYq8fxg0xrFaOKZZD0'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# START कमांड
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "नमस्ते! Koyeb पर Webhook से जुड़ गया हूँ!")

# Webhook से अपडेट लें
@app.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

# Root URL पर webhook सेट करें
@app.route('/')
def index():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://small-kiley-santoshh-f856e5f5.koyeb.app/{API_TOKEN}")
    return "Webhook सेट कर दिया गया!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
user_ids = set()

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
    user_ids.add(message.chat.id)

@bot.message_handler(commands=['bol'])
def handle_bol(message):
    text = message.text.replace("/bol", "").strip()
    if not text:
        bot.reply_to(message, "कृपया कोई टेक्स्ट दें।")
        return
    tts = gTTS(text=text, lang='hi')
    filename = "bol.mp3"
    tts.save(filename)
    with open(filename, "rb") as f:
        bot.send_voice(message.chat.id, f)
    os.remove(filename)

@bot.message_handler(commands=['speak'])
def handle_speak(message):
    text = message.text.replace("/speak", "").strip()
    if not text:
        bot.reply_to(message, "Please provide some text.")
        return
    tts = gTTS(text=text, lang='en')
    filename = "speak.mp3"
    tts.save(filename)
    with open(filename, "rb") as f:
        bot.send_voice(message.chat.id, f)
    os.remove(filename)

@bot.message_handler(commands=['txt'])
def handle_txt(message):
    text = message.text.replace("/txt", "").strip()
    if not text:
        bot.reply_to(message, "कृपया कुछ टेक्स्ट दें।")
        return
    filename = "message.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, "rb") as f:
        bot.send_document(message.chat.id, f)
    os.remove(filename)

@bot.message_handler(commands=['totalusers'])
def handle_total_users(message):
    admin_id = int(os.getenv("ADMIN_ID", "0"))
    if message.from_user.id != admin_id:
        bot.reply_to(message, "आपके पास यह कमांड चलाने की अनुमति नहीं है।")
        return
    total_users = len(user_ids)
    bot.reply_to(message, f"Bot ke saath ab tak {total_users} users ne interact kiya hai.")

@bot.message_handler(commands=['broadcast'])
def handle_broadcast(message):
    admin_id = int(os.getenv("ADMIN_ID", "0"))
    if message.from_user.id != admin_id:
        bot.reply_to(message, "आपके पास यह कमांड चलाने की अनुमति नहीं है।")
        return
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        bot.reply_to(message, "कृपया मैसेज दें जो ब्रॉडकास्ट करना है।")
        return
    msg = text[1]
    success, fail = 0, 0
    for uid in list(user_ids):
        try:
            bot.send_message(uid, msg)
            success += 1
        except:
            fail += 1
    bot.reply_to(message, f"Broadcast sent to {success} users, failed for {fail}.")

bot.infinity_polling()
