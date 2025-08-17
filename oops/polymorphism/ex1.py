class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"
    
    def __add__(self,other):
        return self.price+other.price
    
class EBook(Book):
    def __init__(self,title,author,price,file_size):
        super().__init__(title,author,price)
        self.file_size=file_size

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, Price: {self.price}, File Size: {self.file_size}MB"

class PrintedBook(Book):
    def __init__(self,title,author,price,pages):
        super().__init__(title,author,price)
        self.pages=pages

    def get_info(self):
        return f"PrintedBook: {self.title}, Author: {self.author}, Price: {self.price}, Pages: {self.pages}"
    
def show_book_details(book):
    print(book.get_info())

b1=EBook("Concepts","Lovenesh",200,34)
show_book_details(b1)