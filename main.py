
import telebot
import random

# === CONFIG ===
import os
API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# === INITIALIZE ===
bot = telebot.TeleBot(API_TOKEN)

# === TEMP PROXY LIST (for testing) ===
proxy_list = [
    "http://user1:pass1@123.123.123.123:8080",
    "http://user2:pass2@124.124.124.124:8081",
    "http://user3:pass3@125.125.125.125:8082"
]

# === START COMMAND ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "📶 Добро пожаловать в магазин прокси!\nНажми /buy чтобы купить прокси.")

# === BUY COMMAND ===
@bot.message_handler(commands=['buy'])
def send_proxy(message):
    if len(proxy_list) == 0:
        bot.send_message(message.chat.id, "❌ Прокси закончились. Попробуйте позже.")
        return

    proxy = random.choice(proxy_list)
    proxy_list.remove(proxy)
    bot.send_message(message.chat.id, f"📦 Вот ваш прокси:\n<code>{proxy}</code>", parse_mode='HTML')

    # Уведомление админу
    bot.send_message(ADMIN_ID, f"✉️ Новый заказ от @{message.from_user.username or 'пользователь'}\nВыдан прокси: {proxy}")

# === ADMIN ONLY: ADD PROXY ===
@bot.message_handler(commands=['add'])
def add_proxy(message):
    if message.from_user.id != ADMIN_ID:
        return
    proxies = message.text.split('\n')[1:]
    proxy_list.extend(proxies)
    bot.send_message(message.chat.id, f"✅ Добавлено {len(proxies)} прокси.")

# === RUN ===
bot.polling(none_stop=True)
