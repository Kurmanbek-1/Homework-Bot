from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storege = MemoryStorage()

TOKEN = config('TOKEN')

Bot = Bot(TOKEN)
dp = Dispatcher(bot=Bot, storage=storege)
Admins = (995712956, )