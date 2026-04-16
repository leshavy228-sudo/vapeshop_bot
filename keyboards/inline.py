from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

for_cmd_ubout = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = "Наш канал",callback_data = 'channel', url= "https://t.me/napaslavandossss")
        ]
    ]
)