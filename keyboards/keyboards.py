from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from lexicon.lexicon import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])
yes_no_kb_builder = ReplyKeyboardBuilder()
yes_no_kb_builder.add(button_yes, button_no)
yes_no_kb_builder.adjust(2)
yes_no_keyboard: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
#one_time_keyboard - кнопки сворачиваются

button_1 = KeyboardButton(text=LEXICON_RU['камень'])
button_2 = KeyboardButton(text=LEXICON_RU['ножницы'])
button_3 = KeyboardButton(text=LEXICON_RU['бумага'])
game_kb_builder = ReplyKeyboardBuilder()
game_kb_builder.row(button_1, button_2, button_3, width=1)
game_keyboard: ReplyKeyboardMarkup = game_kb_builder.as_markup(resize_keyboard=True)
