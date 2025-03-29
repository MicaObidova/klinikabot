import nfc
import requests

BOT_TOKEN = "7800814667:AAGHEwLt-QKOGnHLmEhAZAqlkI4Z7LNv1-Y"
CHAT_ID = "1734408952"

def send_to_telegram(data):
    url = f"https://api.telegram.org/bot{7800814667:AAGHEwLt-QKOGnHLmEhAZAqlkI4Z7LNv1-Y}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"NFC ma'lumotlari: {data}"}
    requests.post(url, data=payload)

def on_connect(tag):
    user_data = tag.ndef.message.pretty()
    print("NFC kartadan o'qildi:", user_data)
    send_to_telegram(user_data)

import telebot

TOKEN = "7800814667:AAGHEwLt-QKOGnHLmEhAZAqlkI4Z7LNv1-Y"
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Klinikamizning rasmiy botiga xush kelibsiz, nfc kartangizni kiritdingizmi?")

@bot.message_handler(func=lambda message: True)
def ask_info(message):
    user_id = message.chat.id
    if user_id not in user_data:
        user_data[user_id] = {"nfc_data": message.text}
        bot.send_message(user_id, "Ismingiz va familiyangizni kiriting:")
    elif "name" not in user_data[user_id]:
        user_data[user_id]["name"] = message.text
        bot.send_message(user_id, "Telefon raqamingizni kiriting:")
    elif "phone" not in user_data[user_id]:
        user_data[user_id]["phone"] = message.text
        bot.send_message(user_id, "Yashash manzilingizni kiriting:")
    elif "address" not in user_data[user_id]:
        user_data[user_id]["address"] = message.text
        bot.send_message(user_id, "Qanday kasalliklaringiz bor?")
    else:
        user_data[user_id]["illness"] = message.text
        save_to_file(user_data[user_id])
        bot.send_message(user_id, "Rahmat! Ma'lumotlaringiz saqlandi. Siz bilan tez orada aloqaga chiqamiz")
        del user_data[user_id]


def save_to_file(data):
    with open("users_data.csv", "a", encoding="utf-8") as file:
        file.write(f"{data['nfc_data']},{data['name']},{data['phone']},{data['address']},{data['illness']}\n")


bot.polling()

