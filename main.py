import random
from config import load_config
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, BaseFilter, KICKED, MEMBER
from aiogram.types import Message, ChatMemberUpdated

config = load_config()
BOT_TOKEN = config.telegram_bot.token
ADMINS = config.telegram_bot.admin_ids

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
