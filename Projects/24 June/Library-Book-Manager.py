class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self.__copies = copies

    @property
    def available(self):
        return self.__copies

    def checkout(self, n):
        if n > self.__copies:
            raise ValueError("Not enough copies")
        self.__copies -= n

    def return_book(self, n):
        self.__copies += n

b1 = Book("123-ABC", "Python Basics", "Author X", 5)
b1.checkout(2)
print(f"Available: {b1.available}")