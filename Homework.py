from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from random import choice
from keyboards.client_kb import start_markup


TOKEN = config('TOKEN') 

Bot = Bot(TOKEN)
dp = Dispatcher(bot=Bot)
Admins = (995712956, )


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await Bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.first_name}",
                           reply_markup=start_markup)




@dp.message_handler(commands=['info'])
async def info_handler(message: types.Message):
    await message.answer("Я вам не гугл!")


@dp.message_handler(commands=['bin'], commands_prefix='!/')
async def bin_handler(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in Admins:
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await Bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)
    else:
        await message.answer('Пиши в группу')

@dp.message_handler(commands=['game'])
async def game_handler():
    pass

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Дальше!', callback_data='button_1')
    markup.add(button_1)




    question = 'BMW or Mercedes Benz?'
    answers = [
        'BMW',
        'Mercedes Benz',
    ]

    await Bot.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation="IZI",
        open_period=60,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('Дальше!', callback_data='button_2')
    markup.add(button_2)

    questions = 'ЧИ ИЛИ НИ ЧИ !?'
    answers = [
        'ЧИ',
        'НИ ЧИ',
        'Ты че дурак?'
    ]

    photo = open('Media/chi.jpg', 'rb')
    await Bot.send_photo(call.from_user.id, photo=photo)

    await Bot.send_poll(
        call.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="IZI",
        open_period=60,
        reply_markup=markup
    )

@dp.callback_query_handler(text='button_2')
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('Next', callback_data='button_call_3')
    markup.add(button_call_3)

    question = 'Оромо или манты?'
    answer = [
        'Оромо',
        'Манты',
        'И то и то'
    ]

    photo = open('Media/Оромо.jpg', 'rb')
    await Bot.send_photo(call.from_user.id, photo=photo)

    await Bot.send_poll(
        call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="izi",
        open_period=60,
        reply_markup=markup
    )

@dp.callback_query_handler(text='button_call_3')
async def quiz_4(call: types.CallbackQuery):

    question = 'Что он выведет?'
    answer = [
        'Бесконечный цикл слово Hello',
        'Выведет просто Hello'
    ]


    photo = open('Media/code.jpg', 'rb')
    await Bot.send_photo(call.from_user.id, photo=photo)


    await Bot.send_poll(
        call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation="izi",
        open_period=60
    )



@dp.message_handler(commands=['mem'])
async def images_mem(message: types.Message):
    photo = open('Media/Unknown.jpg', 'rb')
    await Bot.send_photo(message.from_user.id, photo=photo)



@dp.message_handler()
async def echo(message: types.Message):
    if message.text.lower() == 'game':
        a = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
        random = choice(a)
        await Bot.send_dice(message.chat.id, emoji=random)
    else:
        await Bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)