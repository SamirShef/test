import telebot

bot = telebot.TeleBot("7427951807:AAGNI3BUMibPfUGIom3i11U7s3W5U53ICpg")
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_subscribed(user_id):
        bot.send_message(chat_id, "Вы подписаны на канал! Вы можете использовать команду /play.")
    else:
        bot.send_message(chat_id, "Для доступа к команде /play подпишитесь на канал @businessempire_tg.")

def user_subscribed(user_id):
    user_channels = bot.get_chat_member(CHANNEL_USERNAME, user_id)
    return user_channels.status == 'member'

@bot.message_handler(commands=['play'])
def handle_play(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Игра начата!")

bot.polling()