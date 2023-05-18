import telebot
from telebot import types
bot = telebot.TeleBot('5748413603:AAF54hDEfJDDHnMwMSz-lemxQ9OdmlJYdYs')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Выберите какой язык программирование вы будете изучать")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_c = types.InlineKeyboardButton(text='C#', callback_data='C#')
        # И добавляем кнопку на экран
        keyboard.add(key_c)
        key_py = types.InlineKeyboardButton(text='Python', callback_data='Python')
        keyboard.add(key_py)
        key_js = types.InlineKeyboardButton(text='JavaScript', callback_data='JavaScript')
        keyboard.add(key_js)
        key_sql = types.InlineKeyboardButton(text='SQL', callback_data='SQL')
        keyboard.add(key_sql)
        key_njs = types.InlineKeyboardButton(text='NODE.JS', callback_data='NODE.JS')
        keyboard.add(key_njs)
        key_php = types.InlineKeyboardButton(text='PHP', callback_data='PHP')
        keyboard.add(key_php)
        key_css = types.InlineKeyboardButton(text='CSS', callback_data='CSS')
        keyboard.add(key_css)
        bot.send_message(message.from_user.id, text='Выберите язык программирование', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Выберите язык программирование ")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(commands=['start'])
def callback_worker(call):
    bot.send_message(call.message.chat.id, get_text_messages)
    if call.data == "C#":
        msg = ("https://proglib.io/p/sql-digest")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "SQL":
        msg = ("https://proglib.io/p/sql-digest")
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
bot.polling(none_stop=True)