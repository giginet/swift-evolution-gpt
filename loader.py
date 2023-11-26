from functools import reduce
from pathlib import Path
from typing import List

from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, StorageContext, \
    load_index_from_storage, LLMPredictor, OpenAIEmbedding, download_loader, Document
from llama_index.indices.base import IndexType
from llama_index.llms import OpenAI

import os
import logging

from llama_index.readers.file.markdown_reader import MarkdownReader


class ProposalsLoader:
    @property
    def cache_path(self) -> str:
        return os.path.join(os.getcwd(), ".caches")

    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        self.llm = OpenAI(model='gpt-4-turbo')

    def load(self) -> IndexType:
        embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
        predictor = LLMPredictor(llm=self.llm)
        service_context = ServiceContext.from_defaults(
            embed_model=embed_model,
            llm_predictor=predictor
        )
        # documents = SimpleDirectoryReader(self.directory_path).load_data()

        markdown_reader = MarkdownReader()
        proposals = [os.path.join(self.directory_path, markdown)
                     for markdown in os.listdir(self.directory_path) if markdown.endswith(".md")]

        def extend_markdowns(list: List[Document], filepath: str) -> List[Document]:
            docs = markdown_reader.load_data(file=Path(filepath))
            list.extend(docs)
            return list

        documents: List[Document] = reduce(
            extend_markdowns,
            proposals,
            []
        )

        if not os.path.exists(self.cache_path):
            print("No caches found. Learning from scratch")
            index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
            index.storage_context.persist(self.cache_path)
        else:
            print("Learned caches found. Loading from caches")
            storage_context = StorageContext.from_defaults(persist_dir=self.cache_path)
            index = load_index_from_storage(storage_context)
        return index