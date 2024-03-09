from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

router = Router()

@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])