import telebot
from telebot import types
bot = telebot.TeleBot('5950307374:AAGyzJHqXuKLcy5BXTxjOvJbmowb2JedndI')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton("МЕНЮ")

    markup.add(item2)

    file = open('img/human.jpg', 'rb')
    bot.send_photo(message.chat.id, file,  "Қош келдіңіз, {0.first_name}!\nМен - <b>{1.first_name}</b>, адам эволюциясы туралы бәрін білетін ботпын. Ұнаса мен сіздің қызметіңізге дайынмын!!! Бастаймыз ба?".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'МЕНЮ':

            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Адам биологиясы", callback_data='biol')
            item2 = types.InlineKeyboardButton("Адамның пайда болуы", callback_data='hist')
            item3 = types.InlineKeyboardButton("Адам санасы", callback_data='filo')
            item4 = types.InlineKeyboardButton("Өркениеттің пайда болуы", callback_data='civil')
            item5 = types.InlineKeyboardButton("Мәдениет", callback_data='kultura')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id,
                             'Адам – ақыл-ойы мен санасы бар қоғамдық тіршілік иесі, қоғамдық-тарихи қызмет пен мәдениеттің субъектісі, хомо сапиенс түріне жатады.')
            bot.send_message(message.chat.id, 'Неден бастағыңыз келеді? Төменде берілген категорияларды таңдаңыз',
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'biol':
                file = open('img/биологиясы.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file,
                               'Қазіргі систематикада Homo sapiens (лат. Homo sapiens) биологиялық түрі сүтқоректілер класының приматтар қатарындағы гоминидтер тұқымдасынан Homo тұқымдасына жатады. \n \n Салыстырмалы түрде үлкен ми, жалпақ тырнақтары және қарама-қарсы бас бармақтары бар бес саусақты ұстайтын қол және кейбір басқа белгілер адамдар мен приматтардың көпшілігіне тән. Салыстырмалы анатомия, физиология, молекулалық биология, иммуногенетика, патология зерттеулерінің нәтижелері бойынша африкалық ұлы маймылдар — шимпанзелер және аз дәрежеде гориллалар — қазіргі адамдарға ең жақын. Адам мен шимпанзенің ДНҚ-сы кем дегенде 98,5% гендерін бөліседі')
            elif call.data == 'hist':
                file = open('img/проис.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file,
                               'Салыстыру ДНК тізбегі адамдардың ең жақын тірі туыстары шимпанзенің екі түрі (жалпы және бонобо) екенін көрсетеді. Филогенетикалық линия, онымен шығу тегі қазіргі адам (Homo sapiens) байланысты, бөлінген басқа гоминидтер 6-7 миллион жыл бұрын (миоценде). Бұл желінің басқа өкілдері (негізінен австралопитектер және гомо тұқымдасының бірқатар түрлері) бүгінгі күнге дейін сақталмаған.')

            elif call.data == 'filo':
                file = open('img/асаны.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file,
                               'Адамның болмысын зерттей отырып, олар көптеген ерекше белгілердің ішінен оның жануарлардан айырмашылығы бойынша шешуші негізгісін табуға тырысады, бұл, мүмкін, соңғы нәтижеде басқалардың бәрін анықтайтын еді. Адамның ең атақты және кең тараған қасиеті – парасаттылықтың болуы, адам «парасатты адам» – (homo sapiens) ретінде анықталады. Адамның тағы бір маңызды анықтамасы жұмыс істеу қабілетімен байланысты, оны гомо фабер – әрекет ететін, өндіретін адам деп атайды. Келесі маңызды ерекшелік - сөйлеудің болуы. \n \n Ертеде ақыл адамды ерекше етеді деп түсінілген. Иудаизмде адамның жақсылық пен жамандықты таңдау еркіндігі бар адам ретіндегі идея пайда болады, оны кейінірек христиандық қабылдады. Еуропадағы Қайта өрлеу дәуірінде пайда болған гуманизм идеясы адамды өзіне тән және өзіндік даралығы бар ең жоғары құндылық ретінде бекітеді.')

            elif call.data == 'civil':
                file = open('img/цивил.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file,
                               'Адамзат өркениетінің ажырамас құрамдас бөліктері әртүрлі дәуірлерде пайда болды. Олардың кейбіреулері гомо сапиенс пайда болғанға дейін көп уақыт бұрын пайда болды.Тас құралдар. Қазіргі кездегі ең көне еңбек құралдары Олдовай шатқалында (Танзания) табылған. Олардың жасы 2,6 миллион жыл деп бағаланады.Өртті меңгеру. Бірқатар археологиялық олжалар гоминидтердің отты кем дегенде 1,6-1,5 және 1 миллион жыл бұрын пайдаланғанын көрсетеді.Өнер.')

            elif call.data == 'kultura':
                file = open('img/культура.jpg', 'rb')
                bot.send_photo(call.message.chat.id, file, 'Жануарлардың көптеген түрлері қарым-қатынаста болса, тіл тек адамға ғана тән, адамзаттың айқындаушы белгісі және жалпы адамзаттық мәдени мұра. Басқа жануарлардың шектеулі жүйелерінен айырмашылығы, адам тілі ашық - таңбалардың шектеулі санын біріктіру арқылы шексіз мағынаны алуға болады.')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="С чего хотите начать?",reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)



