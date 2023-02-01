#=====================================================================================================================
from aiogram.utils import executor
import logging
import asyncio
from config import  dp, Bot, Admins
from handlers import client, callback, extra, admin, fsmAdminMentor, notification
from database.Bot_db import sql_create
from database.Bot_db import register_message_Bot_db

#=====================================================================================================================
async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    await Bot.send_message(chat_id=Admins[0],
                          text="Bot started!")
    sql_create()

#=====================================================================================================================

client.register_handler_client(dp)
callback.register_handlers_callback(dp)
#=============================================================
admin.register_handler_admin(dp)
fsmAdminMentor.register_mentor(dp)
register_message_Bot_db(dp)
notification.register_handler_notification(dp)
#=============================================================
extra.register_handlers_extra(dp)

#=====================================================================================================================

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

#=====================================================================================================================
