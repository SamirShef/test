import client
import telebot

bot = telebot.TeleBot(client.TOKEN)
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите ваш Telegram ID:")
    bot.register_next_step_handler(message, handle_id)

def handle_id(message):
    chat_id = message.chat.id
    user_id = message.text
    bot.send_message(chat_id, f"Ваш Telegram ID: {user_id}")

bot.polling()