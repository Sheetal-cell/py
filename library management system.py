class Library:
  def __init__(self):
    self.no_of_Books = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.no_of_Books = len(self.books)

  def showInfo(self):
    print(f"The library has {self.no_of_Books} books.") 
    print("The books are as follows:-")
    for book in self.books:
      print(book)


obj = Library()
obj.addBook("'Wings of Fire' by Dr. A.P.J. Abdul Kalam")
obj.addBook("'Ignited Minds' by Dr. A.P.J. Abdul Kalam")
obj.addBook("'You Can Win' by Shiv Khera")
obj.addBook("'The 7 Habits of Highly Effective People' (Indian Edition) by Stephen R. Covey")
obj.addBook("'What Young India Wants' by Chetan Bhagat")
obj.addBook("'How to Prepare for Quantitative Aptitude' by Arun Sharma")
obj.addBook("'Word Power Made Easy' by Norman Lewis")
obj.addBook("'The White Tiger' by Aravind Adiga")
obj.addBook("'Train to Pakistan' by Khushwant Singh")
obj.addBook("'Malgudi Days' by R.K. Narayan")
obj.addBook("'Five Point Someone' by Chetan Bhagat")
obj.addBook("'Playing It My Way' by Sachin Tendulkar")
obj.addBook("'An Unsuitable Boy' by Karan Johar")
obj.addBook("'Rich Dad Poor Dad' by Robert Kiyosaki (Indian Edition)")
obj.addBook("'Let's Talk Money' by Monika Halan")
obj.addBook("'Reignited: Scientific Pathways to a Brighter Future' by Dr. A.P.J. Abdul Kalam & Srijan Pal Singh")
obj.addBook("'India 2020: A Vision for the New Millennium' by Dr. A.P.J. Abdul Kalam")
obj.addBook("'Early India: From the Origins to AD 1300' by Romila Thapar")
obj.addBook("'The Argumentative Indian' by Amartya Sen")
obj.addBook("'Why I am an Atheist' by Bhagat Singh")
obj.addBook("'Discovery of India' by Jawaharlal Nehru")
obj.addBook("'Gitanjali' by Rabindranath Tagore")
obj.addBook("'Selected Poems' by Gulzar")
obj.addBook("Amar Chitra Katha Series")
obj.addBook("Sudha Murthy’s Children’s Books")
obj.addBook("'No God in Sight' by Altaf Tyrewala")
obj.addBook("'Godan' by Munshi Premchand")
obj.addBook("'Palace of Illusions' by Chitra Banerjee Divakaruni")
obj.addBook("'Life’s Amazing Secrets' by Gaur Gopal Das")
obj.addBook("'The Monk Who Sold His Ferrari' by Robin Sharma (Indian Edition)")
obj.addBook("'Who Will Cry When You Die?' by Robin Sharma")
obj.showInfo()
    
  
