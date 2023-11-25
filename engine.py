from loader import DirectoryIndexLoader


class SwiftEvolutionEngine:
    def __init__(self):
        self.loader = DirectoryIndexLoader(directory_path="data/swift-evolution")
        index = self.loader.load()
        self.query_engine = index.as_query_engine()

    def ask_to_gpt(self, prompt) -> str:
        response = self.query_engine.query(
            "What is the difference between a struct and a class?"
        )
        return response



