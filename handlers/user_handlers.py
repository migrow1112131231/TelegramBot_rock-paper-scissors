from aiogram import Router, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, KeyboardButton, KeyboardButtonPollType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
from keyboards import yes_no_keyboard, game_keyboard
import random
from logic.logic import get_bot_choice, get_winner

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_keyboard)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_keyboard)

@router.message(F.text == LEXICON_RU['yes_button'])
async def process_yes_answer(message: Message):
    await message.answer(text=random.choice(LEXICON_RU['yes']), reply_markup=game_keyboard)

@router.message(F.text == LEXICON_RU['no_button'])
async def process_no_answer(message: Message):
    await message.answer(text=random.choice(LEXICON_RU['no']))

@router.message(F.text.in_([LEXICON_RU['камень'], LEXICON_RU['ножницы'], LEXICON_RU['бумага']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["choice_bot"]} '
                         f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice) # камень смайлик, бумага без смайлика
    # - 'bot_won'
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_keyboard)
