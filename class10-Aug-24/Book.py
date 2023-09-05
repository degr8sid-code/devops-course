class Book:
    def __init__(self, title, author, total_copies, lend_copies=0):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.lend_copies = lend_copies

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_total_copies(self):
        return self.total_copies

    def set_total_copies(self, total_copies):
        self.total_copies = total_copies

    def get_lend_copies(self):
        return self.lend_copies

    def set_lend_copies(self, lend_copies):
        self.lend_copies = lend_copies

    def loan(self):
        if self.total_copies > self.lend_copies:
            self.lend_copies += 1
            return True
        else:
            return False

    def return_book(self):
        if self.lend_copies > 0:
            self.lend_copies -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nTotal Copies: {self.total_copies}\nLend Copies: {self.lend_copies}"


# Test the Book class
if __name__ == "__main__":
    book1 = Book("Book 1", "Author 1", 5)
    book2 = Book("Book 2", "Author 2", 3)

    print(book1)
    print()

    print("Loan book1:", book1.loan())
    print("Loan book2:", book2.loan())
    print()

    print(book1)
    print()

    print("Return book1:", book1.return_book())
    print("Return book2:", book2.return_book())
    print()

    print(book1)

