import telebot
from telebot import types

bot = telebot.TeleBot('5748413603:AAF54hDEfJDDHnMwMSz-lemxQ9OdmlJYdYs')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Виды отдыха")
    item2 = types.KeyboardButton("Интересные места")
    item3 = types.KeyboardButton('доп услуги')
    item4 = types.KeyboardButton('Отели')
    item5 = types.KeyboardButton('өзім туралы ақпарат')
    item6 = types.KeyboardButton('бот жайлы ақпарат')
    markup.add(item1, item2, item3, item4, item5, item6)
    photo = open('winter.jpg', 'rb')
    bot.send_photo(message.chat.id, photo,
                   f"Армысын, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nАстана туризм ботына қош келдініз!!",
                   parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
        # if message.text == 'Интересные места':
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     mark = types.InlineKeyboardMarkup()
        #     maup = types.InlineKeyboardMarkup()
        #     ramm = types.InlineKeyboardMarkup()
        #     btn2 = types.InlineKeyboardMarkup()
        #     back = types.KeyboardButton('Бастапқы менюға қайту')
        #     markup.add(back)
        #     mark.add(types.InlineKeyboardButton("Подробнее", url="https://astana.citypass.kz/"))
        #     maup.add(types.InlineKeyboardButton("Подробнее", url="https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%B9%D1%82%D0%B5%D1%80%D0%B5%D0%BA_(%D0%BC%D0%BE%D0%BD%D1%83%D0%BC%D0%B5%D0%BD%D1%82)"))
        #     ramm.add(types.InlineKeyboardButton("Подробнее", url="https://www.vk.com"))
        #     btn2.add(types.InlineKeyboardButton("Подробнее", url="https://e-history.kz/ru/news/show/4745"))
        #     photo = open('expo.jpg', 'rb')
        #     hoto = open('aljir.jpg', 'rb')
        #     iterek= open('baiterek.jpg', 'rb')
        #     museum = open('musek.jpg', 'rb')
        #     bot.send_photo(message.chat.id, photo, "Это Expo 2017, есть развлечения для детей, и можно погулять",
        #                    reply_markup=mark)
        #     bot.send_photo(message.chat.id, iterek, "«Байтерек» — монумент и смотровая башня в столице Казахстана", reply_markup=maup)
        #     bot.send_photo(message.chat.id,museum, "Национальный музей Республики Казахстан самый молодой и "
        #                                                              "самый крупный музей в Центральной Азии. Музей был создан в "
        #                                                              "рамках реализации Государственной программы "
        #                                                              "«Культурное наследие» по поручению Президента Республики "
        #                                                              "Казахстан Н. А. Назарбаева. 2 июля 2013 года вышло Постановление "
        #                                                              "Правительства Республики Казахстан № 675 о создании республиканского "
        #                                                              "государственного учреждения «Национальный музей Республики Казахстан» "
        #                                                              "Министерства культуры Республики Казахстан».", reply_markup=btn2)
        #     bot.send_photo(message.chat.id, hoto, "Это набережная, самый большой парк в Астане, много развлечений, и есть Атырауский мост который подарили на день города в 2018 году", reply_markup=ramm)
        #
        #     bot.send_message(message.chat.id, "давайте вернемся обратно", reply_markup=markup)

        if message.text == 'Интересные места':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            mark = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы менюға қайту')
            next = types.KeyboardButton('жалғастыру')
            markup.add(back, next)
            mark.add(types.InlineKeyboardButton("Подробнее", url="https://astana.citypass.kz/"))
            photo = open('expo.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, "Это Expo 2017, есть развлечения для детей, и можно погулять",reply_markup=mark)
            bot.send_message(message.chat.id, "что вы решили", reply_markup=markup)

        if message.text == 'жалғастыру':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            maup = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы менюға қайту')
            xent = types.KeyboardButton('жалғастыруу')
            maup.add(types.InlineKeyboardButton("Подробнее",
                                                url="https://ru.wikipedia.org/wiki/%D0%91%D0%B0%D0%B9%D1%82%D0%B5%D1%80%D0%B5%D0%BA_(%D0%BC%D0%BE%D0%BD%D1%83%D0%BC%D0%B5%D0%BD%D1%82)"))
            iterek = open('iterek.jpg', 'rb')
            markup.add(back, xent)
            bot.send_photo(message.chat.id, iterek, "«Байтерек» — монумент и смотровая башня в столице Казахстана",
                           reply_markup=maup)
            bot.send_message(message.chat.id, "что вы решили", reply_markup=markup)



        if message.text == 'жалғастыруу':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ramm = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы менюға қайту')
            next = types.KeyboardButton('жалғастыру_3')
            ramm.add(types.InlineKeyboardButton("Подробнее", url="https://e-history.kz/ru/news/show/4745"))
            museum = open('musek.jpg', 'rb')
            bot.send_photo(message.chat.id, museum , "национальный музей Республики Казахстан ", reply_markup=ramm)
            markup.add(back, next)
            bot.send_message(message.chat.id, "что вы решили", reply_markup=markup)

        if message.text == 'жалғастыру_3':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            ramm = types.InlineKeyboardMarkup()
            back = types.KeyboardButton('Бастапқы менюға қайту')
            next = types.KeyboardButton('жалғастыру_3')
            ramm.add(types.InlineKeyboardButton("Подробнее", url="https://e-history.kz/ru/news/show/4745"))
            museum = open('musek.jpg', 'rb')
            bot.send_photo(message.chat.id, museum, "национальный музей Республики Казахстан ", reply_markup=ramm)
            markup.add(back, next)
            bot.send_message(message.chat.id, "что вы решили", reply_markup=markup)


bot.polling(none_stop=True)