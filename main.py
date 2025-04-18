class Library:
    books = {}  # title: Book object

    def __init__(self):
        pass

    @classmethod
    def view_books(cls):
        print("\nAvailable Books:")
        for title, book_obj in cls.books.items():
            if not book_obj.is_borrowed:
                print(f"- {title.title()} by {book_obj.author.title()}")
        print("----------------------------")

    @classmethod
    def get_book(cls, title):
        return cls.books.get(title)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Library.books[self.title] = self

    def borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print("This book is already borrowed!")

    def returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print("This book wasn't borrowed!")


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, title):
        book = Library.get_book(title)
        if book:
            if not book.is_borrowed:
                book.borrowed()
                self.borrowed_books.append(book)
            else:
                print("Sorry, this book is currently not available.")
        else:
            print("Book not found in library.")

    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title == title:
                book.returned()
                self.borrowed_books.remove(book)
                return
        print("You haven't borrowed this book!")


class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, title, author):
        if title in Library.books:
            print("This book already exists in the library!")
        else:
            Book(title, author)
            print(f"'{title}' by {author} added to the library.")


# Example Usage
if __name__ == '__main__':
    admin = Admin("Librarian")
    admin.add_book("Atomic Habits", "James Clear")
    admin.add_book("Do Epic Shit", "Ankur Warikoo")
    admin.add_book("Think and Grow Rich", "Napoleon Hill")
    
    Library.view_books()
    
    user = User("Ali")
    user.borrow_book("Atomic Habits")
    user.borrow_book("Think and Grow Rich")
    Library.view_books()
    
    user.return_book("Atomic Habits")
    Library.view_books()
    
