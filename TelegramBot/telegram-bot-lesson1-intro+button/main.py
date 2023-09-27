import webbrowser
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6475931783:AAEXNtqLL35sdcMiKjImsvwQ6BKkCTDQGKc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    butt1 = types.KeyboardButton('Перейти на сайт')
    butt2 = types.KeyboardButton('Удалить фото')
    butt3 = types.KeyboardButton('Изменить чот')

    markup.row(butt1)
    markup.row(butt2, butt3)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'website is open')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    butt1 = types.InlineKeyboardButton('Перейти на сайт',
                                       url='https://www.youtube.com/watch?v=RpiWnPNTeww&list'
                                           '=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3&ab_channel=ГошаДударь')
    butt2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    butt3 = types.InlineKeyboardButton('Изменить чот', callback_data='edit')

    markup.row(butt1)
    markup.row(butt2, butt3)
    bot.reply_to(message, 'Какое уёбское фото', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name} {message.from_user.last_name} aka {message.from_user.username}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <u><em>informa</em>tion</u>', parse_mode='html')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open(
        'https://www.youtube.com/watch?v=-l_CYgBj4IE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3&ab_channel'
        '=ГошаДударь')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,
                         f'Привет, {message.from_user.first_name} {message.from_user.last_name} aka {message.from_user.username}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')


bot.polling(none_stop=True)
