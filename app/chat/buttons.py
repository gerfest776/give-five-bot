from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

help_button = KeyboardButton("Что делает бот?")
game_button = KeyboardButton("Начать игру")
stat_button = KeyboardButton("Вывести статистику")

base_markup = (
    ReplyKeyboardMarkup(resize_keyboard=True).row(game_button, stat_button).add(help_button)
)
