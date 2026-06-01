class Document:
    def __init__(self, title: str, content: str, category: str):
        if not title:
            raise ValueError("Title cannot be empty")
        
        if not content:
            raise ValueError("Title cannot be empty")

        if not category:
            raise ValueError("Title cannot be empty")
        

        self.title = title
        self.content = content
        self.category = category
