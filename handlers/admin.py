from aiogram import types, Dispatcher
from config import Bot, Admins
from database.Bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
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
async def all_mentors(message: types.Message):
    mentors = await sql_command_all()
    for user in mentors:
        await message.answer(
        f"id - {user[0]} \nname - {user[1]} \ndirection - {user[2]} \n"
        f"age - {user[3]} \ngroup - {user[4]}"
    )

async def delete_FSMCONTEXT_PROXY_STORAGE(message: types.Message):

    if message.from_user.id not in Admins:
        await message.answer('Ты не админ!')

    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(
                f"id - {user[0]} \nname - {user[1]} \ndirection - {user[2]} \n"
                f"age - {user[3]} \ngroup - {user[4]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"delete {user[0]}",
                                         callback_data=f"delete {user[0]}")
            ))

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await Bot.delete_message(call.from_user.id, call.message.message_id)


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(bin_handler, commands=['bin'], commands_prefix='!/')
    dp.register_message_handler(delete_FSMCONTEXT_PROXY_STORAGE, commands=['del'])
    dp.register_message_handler(all_mentors, commands=['all'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))