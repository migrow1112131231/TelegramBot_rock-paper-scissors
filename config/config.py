from environs import Env
from dataclasses import dataclass

@dataclass
class TelegramBot:
    token: str
    admin_ids: 'list[int]'

#db

@dataclass
class Config:
    telegram_bot: TelegramBot
    #db

def load_config() -> Config:

    env = Env()
    env.read_env()

    return Config(telegram_bot=TelegramBot(
        token=env('BOT_TOKEN'),
        admin_ids=list(map(int, env.list('ADMINS')))
    ))
