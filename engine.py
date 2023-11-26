from typing import Generator
from llama_index.memory import ChatMemoryBuffer
from loader import ProposalsLoader

class SwiftEvolutionEngine:
    def __init__(self, database_path):
        self.loader = ProposalsLoader(directory_path=database_path)
        index = self.loader.load()
        memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
        self.chat_engine = index.as_chat_engine(
            chat_mode="best",
            memory=memory,
            context_prompt=(
                "あなたはSwift言語のマスターです。入力したSwift Evolution(SE)を読み、その内容について回答してください。"
                "多くの質問はSwiftに関しての質問ですので、暗黙的にSwift言語についての内容を回答してください"
            ),
        )

    def ask_to_gpt(self, prompt) -> Generator[str, None, None]:
        response = self.chat_engine.stream_chat(prompt)
        return response.response_gen


