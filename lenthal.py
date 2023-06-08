import telebot
from telebot import types

bot = telebot.TeleBot('5552656753:AAGgrgxXsfIY0CJPmsbNhLZo14ZOnvqKqe0')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Каталог")
    btn2 = types.KeyboardButton("Менеджер")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text='{0.first_name}, магазин Ainalaiyn приветствует тебя . Выберите интересующий вас раздел"'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def function(message):
    if (message.text == "Каталог"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Каталог", reply_markup=markup)
        s = open("12.png", 'rb')
        bot.send_photo(message.chat.id, s)
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Губы', callback_data='gubi')
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Глаза', callback_data='glaza')
        keyboard.add(key2)
        key3 = types.InlineKeyboardButton(text='Брови', callback_data='brovi')
        keyboard.add(key3)
        key4 = types.InlineKeyboardButton(text='Лицо', callback_data='liso')
        keyboard.add(key4)
        bot.send_message(message.chat.id, text="Выберите виды которые вы хотите заказать:", reply_markup=keyboard)
    elif (message.text == "Менеджер"):
        keyboard3 = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, text="Спасибо! Ваш менеджер скоро с вами свяжется", reply_markup=keyboard3)

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Каталог")
        btn2 = types.KeyboardButton("Менеджер")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup) \
 \
        @ bot.callback_query_handler(func=lambda call: True)

        def answer(call):
            if message.chat.type == 'private':
                if call.data == 'gubi':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Вернуться в главное меню")
                    markup.add(item1)
                    bot.send_message(message.chat.id, text="Губы", reply_markup=markup)
                    r = open("gub1.png", 'rb')
                    bot.send_photo(message.chat.id, r)
                    bot.send_message(call.message.chat.id, text="4500тг", reply_markup=r)
                    r = open("gub2.png", 'rb')
                    bot.send_photo(message.chat.id, r)
                    bot.send_message(call.message.chat.id, text="4600тг", reply_markup=r)
                    r = open("gub3.png", 'rb')
                    bot.send_photo(message.chat.id, r)
                    bot.send_message(call.message.chat.id, text="4500тг", reply_markup=r)

                elif call.data == 'glaza':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Вернуться в главное меню")
                    markup.add(item1)
                    bot.send_message(message.chat.id, text="Глаза", reply_markup=markup)
                    e = open("glaz1.png", 'rb')
                    bot.send_photo(message.chat.id, e)
                    bot.send_message(call.message.chat.id, text="5000тг", reply_markup=e)
                    e = open("glaz2.png", 'rb')
                    bot.send_photo(message.chat.id, e)
                    bot.send_message(call.message.chat.id, text="5000тг", reply_markup=e)

                elif call.data == 'brovi':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Вернуться в главное меню")
                    markup.add(item1)
                    bot.send_message(message.chat.id, text="Брови", reply_markup=markup)
                    w = open("b1.png", 'rb')
                    bot.send_photo(message.chat.id, w)
                    bot.send_message(call.message.chat.id, text="3700тг", reply_markup=w)
                    w = open("b2.png", 'rb')
                    bot.send_photo(message.chat.id, w)
                    bot.send_message(call.message.chat.id, text="4000тг", reply_markup=w)
                    w = open("b3.png", 'rb')
                    bot.send_photo(message.chat.id, w)
                    bot.send_message(call.message.chat.id, text="4000тг", reply_markup=w)

                elif call.data == 'liso':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton("Вернуться в главное меню")
                    markup.add(item1)
                    bot.send_message(message.chat.id, text="Лицо", reply_markup=markup)
                    q = open("l1.png", 'rb')
                    bot.send_photo(message.chat.id, q)
                    bot.send_message(call.message.chat.id, text="6000тг", reply_markup=q)
                    q = open("l1.png", 'rb')
                    bot.send_photo(message.chat.id, q)
                    bot.send_message(call.message.chat.id, text="6000тг", reply_markup=q)
                    q = open("l1.png", 'rb')
                    bot.send_photo(message.chat.id, q)
                    bot.send_message(call.message.chat.id, text="6100тг", reply_markup=q)


                elif (message.text == "Вернуться в главное меню"):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn1 = types.KeyboardButton("Каталог")
                    btn2 = types.KeyboardButton("Менеджер")
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


bot.polling(none_stop=True)