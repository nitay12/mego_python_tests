class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def is_same(self, book):
        return self.name == book.name and self.author == book.author


class Library:
    def __init__(self):
        self.book_arr = []
        self.copy_arr = []
        self.current = 0

    def book_position(self, book):
        for i in range(len(self.book_arr)):
            if self.book_arr[i].is_same(book):
                return i
        return -1

    def add_book(self, book):
        if self.current < 2000:
            index = self.book_position(book)
            if index == -1:
                self.book_arr.append(book)
                self.copy_arr.append(1)
                self.current+=1
            else:
                self.copy_arr[index] += 1

b1 = Book("Harry Potter", "J.K Rolling", 600)
b2 = Book("abc", "N. Caspi", 600)
b3 = Book("abc", "N. Caspi", 600)

print(b1.is_same(b2))
print(b3.is_same(b2))

l1 = Library()
l1.add_book(b1)
l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)
print(l1.book_position(b2))
print(l1.book_arr)
print(l1.copy_arr)