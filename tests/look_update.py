from config import add_config, Config
from aiogram import Bot, Dispatcher
from aiogram.types import Message

config: Config = add_config()
BOT_TOKEN = config.telegram_bot.token
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def look_message(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))

if __name__ == '__main__':
    dp.start_polling(bot)
