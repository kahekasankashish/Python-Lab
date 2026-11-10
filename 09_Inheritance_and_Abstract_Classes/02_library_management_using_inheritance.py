# Q2. Design a Library Management System using inheritance. Create base class LibraryItem with item_id, title and author and display_info(). Create derived classes Book (pages, genre) and Magazine (issue_number, publisher), override display_info(), create objects and display their details.
class LibraryItem:
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author

    def display_info(self):
        print("Item ID:", self.item_id)
        print("Title:", self.title)
        print("Author:", self.author)


class Book(LibraryItem):
    def __init__(self, item_id, title, author, pages, genre):
        super().__init__(item_id, title, author)
        self.pages = pages
        self.genre = genre

    def display_info(self):
        print("Book Details:")
        super().display_info()
        print("Number of pages:", self.pages)
        print("Genre:", self.genre)


class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue_number, publisher):
        super().__init__(item_id, title, author)
        self.issue_number = issue_number
        self.publisher = publisher

    def display_info(self):
        print("Magazine Details:")
        super().display_info()
        print("Issue number:", self.issue_number)
        print("Publisher:", self.publisher)


book = Book(101, "The Alchemist", "Paulo Coelho", 208, "Fiction")
magazine = Magazine(201, "National Geographic", "Various", 125, "National Geographic Partners")

book.display_info()
print()
magazine.display_info()
