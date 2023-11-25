from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, ServiceContext, StorageContext, \
    load_index_from_storage
from llama_index.indices.base import IndexType
from llama_index.llms import OpenAI

import os
import logging


class DirectoryIndexLoader:
    @property
    def cache_path(self) -> str:
        return os.path.join(os.getcwd(), ".caches")

    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        self.llm = OpenAI(temperature=0.1, model='gpt-4')

    def load(self) -> IndexType:
        service_context = ServiceContext.from_defaults(llm=self.llm)
        documents = SimpleDirectoryReader().load_data()

        if not os.path.exists(self.cache_path):
            logging.info("No caches found. Learning from scratch")
            index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
            index.storage_context.persist()
        else:
            logging.info("Learned caches found. Loading from caches")
            storage_context = StorageContext.from_defaults(persist_dir=self.cache_path)
            index = load_index_from_storage(storage_context)
        return index