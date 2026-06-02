from typing import List
from src.knowledge_assistant.document import Document

class KnowledgeBase:
    def __init__(self):
        self.documents: List[Document] = []

    def add_document(self, document: Document):
        self.documents.append(document)

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
