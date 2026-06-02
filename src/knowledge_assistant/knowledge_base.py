from typing import List
from src.decorators.timing import time_execution
from src.decorators.logging import log_call
from src.knowledge_assistant.document import Document

class KnowledgeBase:
    def __init__(self):
        self.documents: List[Document] = []

    def iterate_documents(self):
        for document in self.documents:
            yield document

    @time_execution
    @log_call
    def add_document(self, document: Document):
        self.documents.append(document)

    @time_execution
    @log_call
    def remove_document(self, document: Document):
        self.documents.remove(document)

    def list_documents(self):
        return [
            {
                "title": doc.title,
                "category": doc.category
            }
            for doc in self.documents
        ]
    
    def find_document(self, title: str) -> Document | None:
        normalized = title.strip().lower()

        return next(
            (doc for doc in self.documents
             if doc.title.strip().lower() == normalized), None
        )
    
    def search_documents(self, query: str):
        normalized = query.strip().lower()

        for document in self.documents:
            if (
                normalized in document.title.lower() 
                or normalized in document.content.lower()
            ):
                yield document
