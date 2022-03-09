import telebot

token = '5176752447:AAGaF8CE1L2haI6NMSKaBIoZiH8hVMU1Hb8'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Дарова', 'Прощай')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='ХЗи', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='плохо', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Норм', callback_data=5))
    bot.send_message(message.chat.id, text="Как Дела?", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
    answer = ''
    if call.data == '3':
        answer = 'Пздц'
    elif call.data == '4':
        answer = 'Нет'
    elif call.data == '5':
        answer = 'Вы даун;!'

    bot.send_message(call.message.chat.id, answer)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'дарова':
        bot.send_message(message.chat.id, 'Ку!')
    elif message.text.lower() == 'прощай':
        bot.send_message(message.chat.id, 'Бывай!')
    if message.text.lower()== 'как дела':
        bot.send_message(message.chat.id, 'Отлично!')	
        
           
        
bot.polling(none_stop=True)