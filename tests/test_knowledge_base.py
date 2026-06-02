import pytest
from src.knowledge_assistant.document import Document
from src.knowledge_assistant.knowledge_base import KnowledgeBase


@pytest.fixture
def sample_document():
    return Document(
        "Python OOP",
        "Classes and objects",
        "Programming"
    )

@pytest.fixture
def sample_knowledgebase():
    return KnowledgeBase()

def test_knowledgebase_add_document_successfully(sample_knowledgebase, sample_document):
    sample_knowledgebase.add_document(sample_document)
    
    assert len(sample_knowledgebase.documents) == 1
    assert sample_knowledgebase.documents[0].title == sample_document.title

def test_knowledgebase_remove_document_successfully(sample_knowledgebase, sample_document):
    sample_knowledgebase.add_document(sample_document)
    sample_knowledgebase.remove_document(sample_document)
    
    assert len(sample_knowledgebase.documents) == 0

def test_knowledgebase_list_documents_successfully(sample_knowledgebase, sample_document):
    sample_knowledgebase.add_document(sample_document)
    documents = sample_knowledgebase.list_documents()

    assert len(documents) == 1
    assert documents[0]["title"] == sample_document.title

def test_knowledgebase_find_document_successfully(sample_knowledgebase, sample_document):
    sample_knowledgebase.add_document(sample_document)
    document = sample_knowledgebase.find_document(sample_document.title)
    
    assert document.title == sample_document.title