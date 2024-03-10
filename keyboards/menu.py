from lexicon import LEXICON_MENU
from aiogram import Bot
from aiogram.types import BotCommand

async def main_menu(bot: Bot):
    menu_commands = [BotCommand(
        command=key,
        description=value
    ) for key, value in LEXICON_MENU.items()]
    await bot.set_my_commands(menu_commands)
