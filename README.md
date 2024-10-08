# Library Management System

This is a simple **Library Management System** written in Python. The system allows users to view available books, lend books, return books, and add new books to the library. The system also tracks which user has borrowed a specific book. It demonstrates key **Object-Oriented Programming (OOP)** principles such as **Encapsulation**, **Abstraction**, **Inheritance**, and **Polymorphism** by providing different types of libraries (General, Digital, Academic) with specialized behavior.

## Features

- **Display Books**: View the list of books currently available in the library.
- **Lend Books**: Borrow a book if it is available and not already borrowed by another user.
  - In the Digital Library, the user must pay a subscription fee before borrowing.
  - In the Academic Library, borrowing is time-limited.
- **Return Books**: Return a book that was previously borrowed.
- **Add Books**: Add new books to the library's collection.

## OOP Pillars

1. **Encapsulation**: Book data and lending status are encapsulated within the `Library` class.
2. **Abstraction**: Users interact with the library through methods, without needing to know how the data is managed internally.
3. **Inheritance**: Specialized libraries (`DigitalLibrary`, `AcademicLibrary`) inherit from the base `Library` class.
4. **Polymorphism**: The `lendBook` method is overridden to provide custom behavior for different types of libraries.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository to your local machine or download the `.py` file directly:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   ```
2. Ensure that Python is installed. You can download it from Python's official website.

3. Run the script using Python:

   ```bash
   python library_management.py
   ```

# Usage
When prompted, choose the type of library:

General Library
Digital Library (with subscription fee)
Academic Library (with time-limited borrowing)
After selecting the library type, you can perform the following actions:

Display Books: Lists all the books available in the library.
Lend a Book: Borrow a book by providing the book name and user name.
In the Digital Library, you'll be asked to pay the subscription fee before borrowing.
Add a Book: Add a new book to the library.
Return a Book: Return a borrowed book to make it available again.
You can continue interacting with the library or quit the program at any time.

# Future Enhancements
Borrowing Limits: Limit the number of books a user can borrow at a time.
Due Dates: Implement due dates for borrowed books, with potential late fees.
Book Categories: Allow categorization of books (e.g., fiction, non-fiction, academic).
Graphical User Interface (GUI): Develop a GUI for easier user interaction.
