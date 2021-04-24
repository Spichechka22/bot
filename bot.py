import telebot


bot = telebot.TeleBot('1686472799:AAGWF2uI8_mU3oY4oBr7Iw9YpNZTg0ZoTE0')


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard1.row('Привет', 'Пока', '/command1','/start')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard1)

@bot.message_handler(commands=['command1'])
def command1_message(message):
    bot.send_message (message.chat.id, 'Вот что я могу:\n/command1 - описание\n/command2 - стикер\n/monday, /tuesday, /wednesday, /thursday, /friday, /saturday - рассписание')

@bot.message_handler(commands=['command2'])
def command2_message(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBJYBgcXQpcGsncaRgnZoo0Zf_J_WlnAACSwEAAjDUnREBhYZ3NsTI6R4E")
#ПОНЕДЕЛЬНИК
@bot.message_handler(commands=['monday'])
def monday_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Четная", callback_data=1)
    button2 = telebot.types.InlineKeyboardButton(text="Нечетная", callback_data=2)
    button3 = telebot.types.InlineKeyboardButton(text="Чет/Нечет", callback_data=3)
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.send_message(message.chat.id, "Выбирете неделю", reply_markup=keyboard)

#ВТОРНИК
@bot.message_handler(commands=['tuesday'])
def tuesday_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button4 = telebot.types.InlineKeyboardButton(text="Четная", callback_data=4)
    button5 = telebot.types.InlineKeyboardButton(text="Нечетная", callback_data=5)
    button6 = telebot.types.InlineKeyboardButton(text="Чет/Нечет", callback_data=6)
    keyboard.add(button4)
    keyboard.add(button5)
    keyboard.add(button6)
    bot.send_message(message.chat.id, "Выбирете неделю", reply_markup=keyboard)

#СРЕДА
@bot.message_handler(commands=['wednesday'])
def wednesday_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button7 = telebot.types.InlineKeyboardButton(text="Четная", callback_data=7)
    button8 = telebot.types.InlineKeyboardButton(text="Нечетная", callback_data=8)
    button9 = telebot.types.InlineKeyboardButton(text="Чет/Нечет", callback_data=9)
    keyboard.add(button7)
    keyboard.add(button8)
    keyboard.add(button9)
    bot.send_message(message.chat.id, "Выбирете неделю", reply_markup=keyboard)

#ЧЕТВЕРГ
@bot.message_handler(commands=['thursday'])
def thursday_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button10 = telebot.types.InlineKeyboardButton(text="Четная", callback_data=10)
    button11 = telebot.types.InlineKeyboardButton(text="Нечетная", callback_data=11)
    button12 = telebot.types.InlineKeyboardButton(text="Чет/Нечет", callback_data=12)
    keyboard.add(button10)
    keyboard.add(button11)
    keyboard.add(button12)
    bot.send_message(message.chat.id, "Выбирете неделю", reply_markup=keyboard)
    
#ПЯТНИЦА
@bot.message_handler(commands=['friday'])
def friday_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button13 = telebot.types.InlineKeyboardButton(text="Четная", callback_data=13)
    button14 = telebot.types.InlineKeyboardButton(text="Нечетная", callback_data=14)
    button15 = telebot.types.InlineKeyboardButton(text="Чет/Нечет", callback_data=15)
    keyboard.add(button13)
    keyboard.add(button14)
    keyboard.add(button15)
    bot.send_message(message.chat.id, "Выбирете неделю", reply_markup=keyboard)
    
#СУББОТА
@bot.message_handler(commands=['saturday'])
def saturday_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button16 = telebot.types.InlineKeyboardButton(text="Четная", callback_data=16)
    button17 = telebot.types.InlineKeyboardButton(text="Нечетная", callback_data=17)
    button18 = telebot.types.InlineKeyboardButton(text="Чет/Нечет", callback_data=18)
    keyboard.add(button16)
    keyboard.add(button17)
    keyboard.add(button18)
    bot.send_message(message.chat.id, "Выбирете неделю", reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def handler(call):
    #пн
    if call.data == '1':
        answer = '17:00-18:30 каб.103\nПесочная наб., д.14, лит.А\nРазработка мобильных приложений'
    elif call.data == '2':
        answer = 'Выходной'
    elif call.data == '3':
        answer = 'Четная:\n17:00-18:30 каб.103\nПесочная наб., д.14, лит.А\nРазработка мобильных приложений\n\nНечетная:\nВыходной'
    #вт
    elif call.data == '4':
        answer = '10:00-11:30 каб.1-С::2596\nВяземский пер., д.5-7, лит.А\nФизическая культура\n\n11:40-13:10 каб.201\nПесочная наб., д.14, лит.А\nУчебная практика (разработка, администрирование и защита баз данных)\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nЭкономика отрасли'
    elif call.data == '5':
        answer = '10:00-11:30 каб.1-С::2596\nВяземский пер., д.5-7, лит.А\nФизическая культура\n\n11:40-13:10 каб.201\nПесочная наб., д.14, лит.А\nУчебная практика (разработка, администрирование и защита баз данных)\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nЭкономика отрасли'
    elif call.data == '6':
        answer = 'Четная:\n10:00-11:30 каб.1-С::2596\nВяземский пер., д.5-7, лит.А\nФизическая культура\n\n11:40-13:10 каб.201\nПесочная наб., д.14, лит.А\nУчебная практика (разработка, администрирование и защита баз данных)\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nЭкономика отрасли\n\nНечетная:\n10:00-11:30 каб.1-С::2596\nВяземский пер., д.5-7, лит.А\nФизическая культура\n\n11:40-13:10 каб.201\nПесочная наб., д.14, лит.А\nУчебная практика (разработка, администрирование и защита баз данных)\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nЭкономика отрасли'
    #ср
    elif call.data == '7':
        answer = '13:30-15:00 каб.111\nПесочная наб., д.14, лит.А\nИнструментальные средства разработки программного обеспечения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nОсновы проектирования баз данных\n\n17:00-18:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)'
    elif call.data == '8':
        answer = '10:00-11:30 каб.203\nПесочная наб., д.14, лит.А\nКомпьютерные сети\n\n11:40-13:10 каб.116\nПесочная наб., д.14, лит.А\nРазработка мобильных приложений\n\n13:30-15:00 каб.111\nПесочная наб., д.14, лит.А\nИнструментальные средства разработки программного обеспечения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nОсновы проектирования баз данных\n\n17:00-18:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)'
    elif call.data == '9':
        answer = 'Четная:\n13:30-15:00 каб.111\nПесочная наб., д.14, лит.А\nИнструментальные средства разработки программного обеспечения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nОсновы проектирования баз данных\n\n17:00-18:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\nНечетная:\n10:00-11:30 каб.203\nПесочная наб., д.14, лит.А\nКомпьютерные сети\n\n11:40-13:10 каб.116\nПесочная наб., д.14, лит.А\nРазработка мобильных приложений\n\n13:30-15:00 каб.111\nПесочная наб., д.14, лит.А\nИнструментальные средства разработки программного обеспечения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nОсновы проектирования баз данных\n\n17:00-18:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)'
    #чт
    elif call.data == '10':
        answer = '10:00-11:30 каб.113\nПесочная наб., д.14, лит.А\nРазработка программных модулей (веб-разработка)\n\n11:40-13:10 каб.203\nПесочная наб., д.14, лит.А\nТехнология разработки и защиты баз данных\n\n13:30-15:00 каб.113\nПесочная наб., д.14, лит.А\nСистемное программирование\n\n15:20-16:50 каб.111\nПесочная наб., д.14, лит.А\nИнструментальные средства разработки программного обеспечения\n\n17:00-18:30 каб.116\nПесочная наб., д.14, лит.А\nЧисленные методы'
    elif call.data == '11':
        answer = '10:00-11:30 каб.113\nПесочная наб., д.14, лит.А\nРазработка программных модулей (веб-разработка)\n\n11:40-13:10 каб.203\nПесочная наб., д.14, лит.А\nТехнология разработки и защиты баз данных\n\n13:30-15:00 каб.113\nПесочная наб., д.14, лит.А\nСистемное программирование\n\n15:20-16:50 каб.111\nПесочная наб., д.14, лит.А\nТехнология разработки программного обеспечения\n\n17:00-18:30 каб.116\nПесочная наб., д.14, лит.А\nЧисленные методы'
    elif call.data == '12':
        answer = 'Четная:\n10:00-11:30 каб.113\nПесочная наб., д.14, лит.А\nРазработка программных модулей (веб-разработка)\n\n11:40-13:10 каб.203\nПесочная наб., д.14, лит.А\nТехнология разработки и защиты баз данных\n\n13:30-15:00 каб.113\nПесочная наб., д.14, лит.А\nСистемное программирование\n\n15:20-16:50 каб.111\nПесочная наб., д.14, лит.А\nИнструментальные средства разработки программного обеспечения\n\n17:00-18:30 каб.116\nПесочная наб., д.14, лит.А\nЧисленные методы\n\nНечетная:\n10:00-11:30 каб.113\nПесочная наб., д.14, лит.А\nРазработка программных модулей (веб-разработка)\n\n11:40-13:10 каб.203\nПесочная наб., д.14, лит.А\nТехнология разработки и защиты баз данных\n\n13:30-15:00 каб.113\nПесочная наб., д.14, лит.А\nСистемное программирование\n\n15:20-16:50 каб.111\nПесочная наб., д.14, лит.А\nТехнология разработки программного обеспечения\n\n17:00-18:30 каб.116\nПесочная наб., д.14, лит.А\nЧисленные методы'
    #пт
    elif call.data == '13':
        answer = '10:00-11:30 каб.114\nПесочная наб., д.14, лит.А\n2:Иностранный язык\n\n11:40-13:10 каб.114\nПесочная наб., д.14, лит.А\n2:Иностранный язык\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nПсихология общения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nКомпьютерные сети'
    elif call.data == '14':
        answer = '10:00-11:30 каб.114\nПесочная наб., д.14, лит.А\n1:Иностранный язык\n\n11:40-13:10 каб.114\nПесочная наб., д.14, лит.А\n1:Иностранный язык\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nПсихология общения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nКомпьютерные сети'
    elif call.data == '15':
        answer = 'Четная:\n10:00-11:30 каб.114\nПесочная наб., д.14, лит.А\n2:Иностранный язык\n\n11:40-13:10 каб.114\nПесочная наб., д.14, лит.А\n2:Иностранный язык\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nПсихология общения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nКомпьютерные сети\n\nНечетная:\n10:00-11:30 каб.114\nПесочная наб., д.14, лит.А\n1:Иностранный язык\n\n11:40-13:10 каб.114\nПесочная наб., д.14, лит.А\n1:Иностранный язык\n\n13:30-15:00 каб.206\nПесочная наб., д.14, лит.А\nПсихология общения\n\n15:20-16:50 каб.212\nПесочная наб., д.14, лит.А\nКомпьютерные сети'
    #сб
    elif call.data == '16':
        answer = '10:00-11:30 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n10:00-11:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n11:40-13:10 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n11:40-13:10 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n13:30-15:00 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)'
    elif call.data == '17':
        answer = '10:00-11:30 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n10:00-11:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n11:40-13:10 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n11:40-13:10 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n13:30-15:00 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n'
    elif call.data == '18':
        answer = 'Четная:\n10:00-11:30 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n10:00-11:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n11:40-13:10 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n11:40-13:10 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n13:30-15:00 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\nНечетная:\n10:00-11:30 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n10:00-11:30 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n11:40-13:10 каб.116\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Java)\n\n11:40-13:10 каб.111\nПесочная наб., д.14, лит.А\nРазработка программных модулей(Python)\n\n13:30-15:00 каб.116\nПесочная наб'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message (message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
        bot.send_message (message.chat.id, 'Прощай')
    elif message.text.lower() == 'как дела?':
        bot.send_message (message.chat.id, 'Отлично, рад твоему вопросу)')
    elif message.text.lower() == 'что делаешь?':
        bot.send_message (message.chat.id, 'Жажду помогать людям')
    elif message.text.lower() == 'ляляля':
        bot.send_message (message.chat.id, 'Тополя')
    elif message.text.lower() == 'расскажи анекдот':
        bot.send_message (message.chat.id, 'Колобок повесился')
    elif message.text.lower() == 'расскажи что-нибудь':
        bot.send_message (message.chat.id, 'А больше ничего не хочешь?')
    elif message.text.lower() == 'как дела у анечки?':
        bot.send_message (message.chat.id, 'У Анечки все хорошо, старается!')
    elif message.text.lower() == 'москва заразная?':
        bot.send_message (message.chat.id, 'Она заразительно красива))')
    else:
        bot.send_message (message.chat.id, 'Извини, я слишком глуп')

bot.polling()