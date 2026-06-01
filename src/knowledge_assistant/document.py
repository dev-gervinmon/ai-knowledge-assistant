class Document:

    __allowed_categories = [
        "Programming",
        "AI",
        "DevOps",
        "Database",
        "General"
    ]

    def __init__(self, title: str, content: str, category: str):
        if not title:
            raise ValueError("Title cannot be empty")
        
        if not content:
            raise ValueError("Content cannot be empty")

        if not category:
            raise ValueError("Category cannot be empty")
        
        if category not in self.__allowed_categories:
            raise ValueError(f"Invalid category {category}. " f"Allowed: {self.__allowed_categories}")
        
        self.title = title
        self.content = content
        self.category = category

    def summary(self) -> str:
        if len(self.content) <= 100:
            return self.content
        
        return self.content[:100] + "..."
    
    def update_content(self, updated_content):
        if not isinstance(updated_content, str):
            raise TypeError("content must be a string")
        
        if not updated_content.strip():
            raise ValueError("content cannot be empty")
        
        self.content = updated_content

    def __repr__(self):
        return f"Document(title={self.title}, category={self.category})"
