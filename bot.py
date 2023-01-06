import telebot
from telebot import types

bot = telebot.TeleBot("5808038622:AAECs3mnleoFd-5oO5BIf64svRijY10zsRI")

@bot.message_handler(commands=['start'])
def start(message):
    
    sport_1 = open('FILE 2023-01-06 19:03:18.mp4', 'rb')
    bot.send_video(message.chat.id, sport_1)

    item = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Для парня", callback_data='men')
    item2 = types.InlineKeyboardButton("Для девушки", callback_data='woman')

    item.row(item1)
    item.row(item2)
    bot.send_message(message.chat.id, 'Таксь, а меню для парня или девушки отправлять? Забыл сразу спросить', reply_markup=item)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    
    if call.data == 'men':
        sport1 = open('Меню_для_набора_массы_от_Спартака.pdf', 'rb')
        bot.send_document(call.message.chat.id, sport1)

        sport_1 = open('FILE 2023-01-06 19:03:35.mp4', 'rb')
        video_1 = bot.send_video(call.message.chat.id, sport_1)
        bot.register_next_step_handler(video_1, get_video_1)
        bot.send_message(call.message.chat.id, 'Напишите')



    elif call.data == 'woman':
        sport1 = open('Меню_для_набора_массы_от_Спартака.pdf', 'rb')
        bot.send_document(call.message.chat.id, sport1)

        sport_1 = open('FILE 2023-01-06 19:03:35.mp4', 'rb')
        video_2 = bot.send_video(call.message.chat.id, sport_1)
        bot.register_next_step_handler(video_2, get_video_2)
        bot.send_message(call.message.chat.id, 'Напишите')

def get_video_1(message):
    bot.send_message(message.chat.id, f'Спасибо {message.from_user.first_name}')

def get_video_2(message):
    bot.send_message(message.chat.id, f'Спасибо {message.from_user.first_name}')


bot.polling(none_stop=True)
