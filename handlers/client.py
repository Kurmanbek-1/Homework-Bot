
from config import Bot, Admins
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.client_kb import start_markup

# =====================================================================================================================

async def start_handler(message: types.Message):
    await Bot.send_message(message.from_user.id,
                           f"Hello {message.from_user.first_name}",
                           reply_markup=start_markup)


async def info_handler(message: types.Message):
    await message.answer("Я вам не гугл!")


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


async def images_mem(message: types.Message):
    photo = open('Media/Unknown.jpg', 'rb')
    await Bot.send_photo(message.from_user.id, photo=photo)

# =====================================================================================================================

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(images_mem, commands=['mem'])

# =====================================================================================================================