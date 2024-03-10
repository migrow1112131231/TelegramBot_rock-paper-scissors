from environs import Env
from dataclasses import dataclass

@dataclass
class Telegram_Bot:
    token: str
    admins: 'list[int]'

@dataclass
class Config:
    telegram_bot: Telegram_Bot

def add_config() -> Config:
    env = Env()
    env.read_env()

    return Config(telegram_bot=Telegram_Bot(
        token=env('BOT_TOKEN'),
        admins=list(map(int, env.list('ADMINS')))
    ))
