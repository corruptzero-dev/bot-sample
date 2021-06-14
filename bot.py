import telebot

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def text_handler(message):
   bot.send_message(message.from_user.id, 'Бот работает')
   print(f'Вам написал пользователь с id {message.from_user.id}, имя: {message.from_user.first_name}')
bot.polling()
