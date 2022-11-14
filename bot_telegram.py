import telebot

bot = telebot.TeleBot("5770728377:AAE2rubb764VWeRfSL3hCEUGSMztlEjNps0")

value = ''
old_value = ''

keuboard = telebot.types.InlineKeyboardMarkup()
keuboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('c', callback_data='C'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('/', callback_data='/'))

keuboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'))

keuboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))

keuboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))

keuboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('=', callback_data='='))


@bot.message_handler(commands=['start', 'calculater'])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keuboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keuboard)
@bot.callback_query_handler(func=lambda call:True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка'

    else:
        value += data
    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keuboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keuboard)
            old_value = value

    if value == 'Ошибка': value = ''




bot.polling(none_stop=False, interval=0)

# import logging

# from aiogram import Dispatcher, Bot, types, executor
# from aiogram.dispatcher.filters import Text

# from bas import *

# API_TOKEN = "5585758700:AAF61RsmSXls5Iq4aTPUro4Plet-KDlVqkE"
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# logging.basicConfig(
#     filename = "log.txt",
#     format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level = logging.INFO
# )
# logger = logging.getLogger(__name__)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message; types.Message):
#     kh = [
#         [
#         types.KeyboardButton(text="dice"),
#         types.KeyboardButton(text="цитата")
#         ]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     await message.answer("Hi\nI`m EchoBot!\nPower by aiogram.", reply_markup=keyboard)

# @dp.message_handler(Text(equals="dice"))
# @dp.message_handler(commands=['dice'])
# async def cmd_dice(message: types.Message):
#     msg1 = await message.answer_dice(emoji='=)')
#     logger.info(f'{message.from_user.first_name}, выкинул на кубике {msg1.dice.value}')






# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor

# import os



# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)

# @dp.message_handler()
# async def echo_send(message : types.Message):
#     await message.answer(message.text)



# executor.start_polling(dp, skip_updates=True)