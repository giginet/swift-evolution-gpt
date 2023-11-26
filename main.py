from dotenv import load_dotenv
from bot import Bot

import os

load_dotenv()

if __name__ == '__main__':
    database = os.path.join(os.path.dirname(__file__), 'swift-evolution', 'proposals')

    bot = Bot(database_path=database)
    while True:
        bot.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
