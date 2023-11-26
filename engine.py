from typing import Generator

from loader import ProposalsLoader


class SwiftEvolutionEngine:
    def __init__(self, database_path):
        self.loader = ProposalsLoader(directory_path=database_path)
        index = self.loader.load()
        self.chat_engine = index.as_chat_engine(
            chat_mode="best",
            context_prompt=(
                "You are Swift master. Your duty is answering questions refer the Swift Evolution"
            ),
        )

    def ask_to_gpt(self, prompt) -> Generator[str, None, None]:
        response = self.chat_engine.stream_chat(prompt)
        return response.response_gen


