import aioschedule
from aiogram import types, Dispatcher
from config import Bot
import asyncio



chat_id = []

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = []
    chat_id.append(message.from_user.id)
    await message.answer("Ok")


async def go_to_curses():
    for id in chat_id:
        await Bot.send_message(id, "Пора на курсы!")


async def scheduler():
    aioschedule.every().monday.at('17:00').do(go_to_curses)
    aioschedule.every().thursday.at('17:00').do(go_to_curses)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'напомни' in word.text)