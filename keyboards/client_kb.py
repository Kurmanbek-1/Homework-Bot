# =====================================================================================================================
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# =====================================================================================================================
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=3
)




# =====================================================================================================================
start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz')
mem_button = KeyboardButton('/mem')

share_location = KeyboardButton('Share location', request_location=True) # Кнопка для отправки своей локации
share_contact = KeyboardButton('Share contact', request_contact=True)

bin_chats = KeyboardButton('!bin')

reg_mentor = KeyboardButton('/reg_mentor')
get_mentor = KeyboardButton('/get')
all_mentor = KeyboardButton('/all')
del_mentor = KeyboardButton('/del')

# =====================================================================================================================

# Добавление кнопок
start_markup.add(start_button, info_button, quiz_button, mem_button, share_location, share_contact, reg_mentor,
                 get_mentor, all_mentor, del_mentor, bin_chats)

# =====================================================================================================================
submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton('да'),
    KeyboardButton('нет')
)
cancel_button = KeyboardButton('Cancel')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    cancel_button
)
# =====================================================================================================================