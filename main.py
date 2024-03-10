import asyncio
from config import add_config, Config
from aiogram import Bot, Dispatcher
from handlers import user_handlers, other_handlers
from keyboards import main_menu


async def main():
    config: Config = add_config()
    bot = Bot(token=config.telegram_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    await main_menu(bot=bot)


    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
