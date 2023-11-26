from engine import SwiftEvolutionEngine


class Bot:
    def __init__(self, database_path: str):
        self.engine = SwiftEvolutionEngine(database_path=database_path)

    def run(self):
        while True:
            question = input("User: ")
            if question == "exit": break
            for answer in self.engine.ask_to_gpt(question):
                print(answer, end='')
            print("\n")