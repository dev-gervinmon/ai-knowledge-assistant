from typing import List

from knowledge_assistant.document import Document

class KnowledgeBase:
    def __init__(self):
        self.documents: List[Document] = []