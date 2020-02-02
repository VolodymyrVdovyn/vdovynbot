import telebot
import config
import random
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🎲 Побажання для тебе')
    item2 = types.KeyboardButton('😊 Як справи?')
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, 'Привіт, {0.first_name}!\nЯ - {1.first_name}, тут для того щоб підняти тобі настрій'.format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Побажання для тебе':
            k = random.randint(1,101)
            with open ('prediction', 'r') as inf:
                for i in range(k):
                    s = inf.readline().strip()
            bot.send_message(message.chat.id, s)
        elif message.text == '😊 Як справи?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Добре', callback_data='good')
            item2 = types.InlineKeyboardButton('Не дуже', callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Класноб ти як?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Навіть не знаю що сказати 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Я радий 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Не переживай, випий чаю та з\'їж цукерку')
 
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
 
           
    except Exception as e:
        print(repr(e))
 
bot.polling(none_stop=True)