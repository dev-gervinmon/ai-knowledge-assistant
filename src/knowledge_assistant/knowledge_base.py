from typing import List

from knowledge_assistant.document import Document

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
