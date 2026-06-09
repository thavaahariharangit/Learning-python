class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"
    
# shelf = BookShelf(500)
# print(shelf)

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"'{self.title}'"
    
book = Book("The Great Gatsby")
book2 = Book("To Kill a Mockingbird")
shelf = BookShelf(book, book2)
print(shelf)