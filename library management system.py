class Library:
  def __init__(self):
    self.no_of_Books = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.no_of_Books = len(self.books)

  def showInfo(self):
    print(f"The library has {self.no_of_Books} books. The books are")
    for book in self.books:
      print(book)


obj = Library()
obj.addBook("Harry Potter1")
obj.addBook("Harry Potter2")
obj.addBook("Harry Potter3")
obj.showInfo()
    
  
