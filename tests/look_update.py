import random
from environs import Env
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, BaseFilter, KICKED, MEMBER
from aiogram.types import Message, ChatMemberUpdated

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def look_message(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))

if __name__ == '__main__':
    dp.run_polling(bot)