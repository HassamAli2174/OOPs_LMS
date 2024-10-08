# Base Class: Library
class Library:
    def __init__(self, book_list, library_name):
        self.__bookList = book_list  # Encapsulation: Keeping book list private
        self.__name = library_name   # Encapsulation
        self.__lendDict = {}         # Encapsulation
    
    def displayBooks(self):
        print(f'Welcome to {self.__name} Library. We have the following books available:')
        for sno, book in enumerate(self.__bookList, start=1):
            print(f'{sno}. {book}')
    
    def lendBook(self, book, user_name):
        if book in self.__bookList:
            if book not in self.__lendDict:
                self.__lendDict.update({book: user_name})
                print(f'Lender-Book database has been updated. {user_name}, you can take the book "{book}" now.')
            else:
                print(f'Sorry, the book "{book}" is already borrowed by {self.__lendDict[book]}.')
        else:
            print(f'The book "{book}" is not available in the library.')
    
    def addBook(self, book):
        self.__bookList.append(book)
        print(f'The book "{book}" has been added to the library.')
        
    def returnBook(self, book):
        if book in self.__lendDict:
            self.__lendDict.pop(book)
            print(f'The book "{book}" has been returned successfully.')
        else:
            print(f'The book "{book}" was not borrowed.')

# Derived Class: DigitalLibrary using Inheritance
class DigitalLibrary(Library):
    def __init__(self, book_list, library_name, subscription_fee):
        super().__init__(book_list, library_name)  # Inheriting from Library
        self.subscription_fee = subscription_fee   # Additional attribute
    
    # Method Overriding (Polymorphism)
    def lendBook(self, book, user_name):
        print(f'{user_name}, please pay the subscription fee of {self.subscription_fee} before borrowing.')
        super().lendBook(book, user_name)

# Derived Class: AcademicLibrary using Inheritance and Polymorphism
class AcademicLibrary(Library):
    def lendBook(self, book, user_name):
        print(f'{user_name}, you can only borrow academic books for 7 days.')
        super().lendBook(book, user_name)

# Execution work
if __name__ == '__main__':
    print("Choose the type of library:")
    print("1. General Library")
    print("2. Digital Library")
    print("3. Academic Library")

    library_choice = input()
    
    if library_choice == '1':
        HassamLibrary = Library(['Python', 'Data Scraping', 'Java', 'Web Scraping', 'Complier Construction'], 'Hassam')
    elif library_choice == '2':
        subscription_fee = float(input('Enter the subscription fee for Digital Library: '))
        HassamLibrary = DigitalLibrary(['Python', 'AI for All', 'Machine Learning'], 'Digital Learning', subscription_fee)
    elif library_choice == '3':
        HassamLibrary = AcademicLibrary(['Data Structures', 'Algorithms', 'Complier Design'], 'University Library')
    else:
        print("Invalid library choice.")
        exit()

    while True:
        print(f'\nWelcome to the {HassamLibrary._Library__name} Library. Enter your choice to continue:')
        print('1. Display Books')
        print('2. Lend a Book')
        print('3. Add a Book')
        print('4. Return a Book')
        
        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print('Please enter a valid option')
            continue
        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            HassamLibrary.displayBooks()
            
        elif user_choice == 2:
            book = input('Enter the name of the book you want to lend: ')
            user_name = input('Enter your name: ')
            HassamLibrary.lendBook(book, user_name)
        
        elif user_choice == 3:
            book = input('Enter the name of the book you want to add: ')
            HassamLibrary.addBook(book)
            
        elif user_choice == 4:
            book = input('Enter the name of the book you want to return: ')
            HassamLibrary.returnBook(book)
        
        else:
            print('Invalid choice')

        print('\nPress "q" to quit or "c" to continue:')
        
        user_choice2 = ''
        
        while user_choice2 not in ['c', 'q']:
            user_choice2 = input()
            if user_choice2 == 'q':
                print("Thank you for using the library system. Goodbye!")
                exit()
            if user_choice2 == 'c':
                continue
