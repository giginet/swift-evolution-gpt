from dotenv import load_dotenv
from engine import SwiftEvolutionEngine

import os

load_dotenv()

if __name__ == '__main__':
    database = os.path.join(os.path.dirname(__file__), 'fixtures', 'light_data')
    engine = SwiftEvolutionEngine(database_path=database)

    while True:
        question = input("User: ")
        if question == "exit":
            break
        answer = engine.ask_to_gpt(question)
        print("\n")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
