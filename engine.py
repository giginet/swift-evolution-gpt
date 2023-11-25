from loader import DirectoryIndexLoader


class SwiftEvolutionEngine:
    def __init__(self, database_path):
        self.loader = DirectoryIndexLoader(directory_path=database_path)
        index = self.loader.load()
        self.query_engine = index.as_query_engine()

    def ask_to_gpt(self, prompt) -> str:
        response = self.query_engine.query(prompt)
        return response



