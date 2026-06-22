class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False 

    def display_info(self):
        status = "is currently borrowed" if self.is_borrowed else "is available"
        print(f"'{self.title}' by {self.author} {status}.")

book1 = Book("Devdas", "Sarat Chandra Chattopadhyay")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Atomic Habits", "James Clear")

book2.is_borrowed = True

book1.display_info()
book2.display_info()
book3.display_info()