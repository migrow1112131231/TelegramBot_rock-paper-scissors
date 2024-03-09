import random
from lexicon import LEXICON_RU

# получаем рандомно: камень, ножницы, бумага
def get_bot_choice() -> None:
    return random.choice(LEXICON_RU['random_choice_game'])


def get_winner(user_choice: str, bot_choice: str) -> str:
    # user choice - камень 🗿 и тд
    # bot choice - get_bot_choice() func - камень, ножницы, бумага
    bot_choice = LEXICON_RU[bot_choice] # получим + смайлик
    # теперь у нас user_choice и bot_choice равны
    rules = {'Камень 🗿': 'Ножницы ✂',
             'Ножницы ✂': 'Бумага 📜',
             'Бумага 📜': 'Камень 🗿'}
    if user_choice == bot_choice:
        return 'draw'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'