import pytest
from src.knowledge_assistant.document import Document

@pytest.fixture
def sample_document():
    return Document(
        "Python OOP",
        "Classes and objects",
        "Programming"
    )

def test_create_document_successfully(sample_document):
    assert sample_document.title == "Python OOP"
    assert sample_document.content == "Classes and objects"
    assert sample_document.category == "Programming"

def test_document_rejects_empty_title():
    with pytest.raises(ValueError):
        Document(
            "",
            "Classes and objects",
            "Programming"
        )

def test_document_rejects_empty_content():
    with pytest.raises(ValueError):
        Document(
            "Python OOP",
            "",
            "Programming"
        )


def test_document_rejects_empty_category():
    with pytest.raises(ValueError):
        Document(
            "Python OOP",
            "Classes and objects",
            ""
        )

def test_document_rejects_invalid_category():
    with pytest.raises(ValueError):
        Document(
            "Python OOP",
            "Classes and objects",
            "Test"
        )

def test_document_check_summary_count():
    document = Document(
        "Python OOP",
        "Pariatur duis occaecat cupidatat labore amet culpa commodo ut pariatur nisi est. Mollit amet duis do pariatur minim cupidatat exercitation amet laborum ut amet. Exercitation deserunt adipisicing ea eu magna ut sit occaecat. Aute sint pariatur ea esse velit incididunt duis excepteur aliquip consequat reprehenderit. Labore quis labore minim labore sint velit dolore aliquip tempor esse non culpa. Veniam Lorem in incididunt dolor. Velit pariatur est incididunt proident ea Lorem do pariatur excepteur ipsum laboris veniam pariatur Lorem.",
        "Programming"
    )

    summary = document.summary()
    assert len(summary) == 103

def test_document_update_content_successfully(sample_document):

    sample_document.update_content("Updated content")
    assert sample_document.content == "Updated content"

def test_document_invalid_update_content(sample_document):
    with pytest.raises(TypeError):
        sample_document.update_content(35)

    with pytest.raises(ValueError):
        sample_document.update_content("")
