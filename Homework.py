from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config('TOKEN') 

Bot = Bot(TOKEN)
dp = Dispatcher(bot=Bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await Bot.send_message(message.from_user.id,
                           f"Hello chort {message.from_user.first_name}")
    await message.answer("This is an answer method!")
    await message.reply("This is a reply method")



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
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
    )


@dp.message_handler(commands=['mem'])
async def images_mem(message: types.Message):
    photo = open('Media/Unknown.jpg', 'rb')
    await Bot.send_photo(message.from_user.id, photo=photo)



@dp.message_handler()
async def echo(message: types.Message):
    await Bot.send_message(message.from_user.id, int(message.text)**2)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)