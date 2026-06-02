import pytest
from src.knowledge_assistant.document import Document
from src.knowledge_assistant.knowledge_base import KnowledgeBase


@pytest.fixture
def sd():
    return Document(
        "Python OOP",
        "Classes and objects",
        "Programming"
    )

@pytest.fixture
def skb():
    return KnowledgeBase()

def test_knowledgebase_add_document_successfully(skb, sd):
    skb.add_document(sd)
    
    assert len(skb.documents) == 1
    assert skb.documents[0].title == sd.title

def test_knowledgebase_remove_document_successfully(skb, sd):
    skb.add_document(sd)
    skb.remove_document(sd)
    
    assert len(skb.documents) == 0

def test_knowledgebase_list_documents_successfully(skb, sd):
    skb.add_document(sd)
    documents = skb.list_documents()

    assert len(documents) == 1
    assert documents[0]["title"] == sd.title

def test_knowledgebase_find_document_successfully(skb, sd):
    skb.add_document(sd)
    document = skb.find_document(sd.title)
    
    assert document.title == sd.title

def test_knowledgebase_iterate_documents_successfully(skb, sd):
    sd2 = Document(
        "Docker",
        "Containers",
        "DevOps",
    )

    skb.add_document(sd)
    skb.add_document(sd2)

    documents = list(skb.iterate_documents())

    assert len(documents) == 2
    assert documents[0].title == sd.title
    assert documents[1].title == sd2.title