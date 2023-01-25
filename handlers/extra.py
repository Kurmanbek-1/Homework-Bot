from aiogram import types, Dispatcher
from config import Bot
from random import choice



async def echo(message: types.Message):
    bad_words = ['bitch', 'fake', 'дурак', "дура", 'идиот', 'урод']
    username = f'@{message.from_user.username}' \
        if message.from_user.username is not None else message.from_user.first_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
                await message.answer(f'Не матерись {username}\n'
                                     f'Сам ты {word}!')

    if message.text.lower() == 'game':   # Игра работает для всех!
        a = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
        random = choice(a)
        await Bot.send_dice(message.chat.id, emoji=random)
    else:
        await Bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)