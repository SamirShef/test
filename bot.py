import telebot

bot = telebot.TeleBot("7427951807:AAE_dNHJ2tT0BCXvNOPJK9sQ-8KlgKMJ0h8")
@bot.message_handler(commands=['start'])
def start(message):
    # Отправляем сообщение с просьбой отправить свой ID
    bot.send_message(message.chat.id, "Привет! Чтобы получить свой Telegram ID, нажмите на кнопку ниже.", reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, "Нажмите на кнопку 👇", reply_markup=types.ForceReply())

@bot.message_handler(func=lambda message: True)
def get_user_id(message):
    # Отправляем сообщение с ID пользователя
    bot.send_message(message.chat.id, f"Ваш Telegram ID: {message.from_user.id}")

@bot.message_handler(commands=['check_subscription'])
def check_subscription(message):
    # Проверяем подписку пользователя на канал @businessempire_tg
    user_id = message.from_user.id
    is_subscribed = bot.get_chat_member('@businessempire_tg', user_id).status == 'member'
    if is_subscribed:
        bot.send_message(message.chat.id, "Вы подписаны на канал @businessempire_tg")
    else:
        bot.send_message(message.chat.id, "Вы не подписаны на канал @businessempire_tg")

# Запуск бота
bot.polling()