from aiogram import types, Dispatcher
from config import Bot, Admins


async def bin_handler(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in Admins:  # Закреплять сообщения могут только админы
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await Bot.pin_chat_message(message.chat.id,
                                       message.reply_to_message.message_id)
    else:
        await message.answer('Пиши в группу')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(bin_handler, commands=['bin'], commands_prefix='!/')