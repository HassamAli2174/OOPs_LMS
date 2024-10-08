class Library:
    def __init__(self, book_list, library_name):
        self.bookList = book_list
        self.name = library_name
        self.lenDict = {}  # To track which user has borrowed which book
        
    def displayBooks(self):
        print(f'Welcome to {self.name} Library. We have the following books available:')
        for sno, book in enumerate(self.bookList, start=1):
            print(f'{sno}. {book}')
    
    def lendBook(self, book, borrower_name):
        if book in self.bookList:
            if book not in self.lenDict:
                self.lenDict.update({book: borrower_name})
                print(f'Lender-Book database has been updated. {borrower_name}, you can take the book "{book}" now.')
            else:
                print(f'Sorry, the book "{book}" is already borrowed by {self.lenDict[book]}.')
        else:
            print(f'The book "{book}" is not available in the library.')
    
    def addBook(self, book):
        self.bookList.append(book)
        print(f'The book "{book}" has been added to the library.')
        
    def returnBook(self, book):
        if book in self.lenDict:
            self.lenDict.pop(book)
            print(f'The book "{book}" has been returned successfully.')
        else:
            print(f'The book "{book}" was not borrowed.')

# Sample library usage
library = Library(['Python', 'Data Scraping', 'Java'], 'Hassam')

# Display books
library.displayBooks()

# Lending a book
library.lendBook('Python', 'John')

# Trying to lend the same book again
library.lendBook('Python', 'Alice')

# Returning a book
library.returnBook('Python')

# Trying to return a book that wasn't borrowed
library.returnBook('Data Scraping')
