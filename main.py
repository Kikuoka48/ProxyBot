import os
import telebot

# Получаем токен из переменной окружения
API_TOKEN = os.getenv("BOT_TOKEN")

if not API_TOKEN:
    raise ValueError("❌ Переменная окружения BOT_TOKEN не установлена!")

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет! Бот работает на Railway!")

# Запуск бота
bot.polling(none_stop=True)
