# Module for the library management system: storing and interacting with library data such as books, users, authors, and genres.  

from libraryClasses import Genre, Book, User, Author

books = {}
users = {}
authors = {}
genres = {}

def addBook(title, author, ISBN, publication_date, genre_name, genre_description, genre_category):
    try:
        new_book = Book(title, author, ISBN, publication_date, "Available", genre_name, genre_description, genre_category)
        books.update({ISBN: new_book})
        print("Added new book!")
    except Exception as e:
        print(f"Error occurred: {e}")

def borrowBook(user_id, ISBN):
    try:
        book = books.get(ISBN, None)
        if book is None:
            return("Book with this ISBN does not exist.")
        if book.getAvailability() == "Borrowed":
            return("This book is checked out.")
        user = users.get(user_id, None)
        if user is None:
            return("User with this ID does not exist.")
        book.setAvailability("Borrowed")
        user.addBorrowedBook(ISBN, book.getTitle())
        return(f"User {user_id} borrowed book {book.getTitle()}")
    except Exception as e:
        print(f"Error occurred: {e}")

def returnBook(user_id, ISBN):
    try:
        book = books.get(ISBN, None)
        if book is None:
            return("Book with this ISBN does not exist.")
        if book.getAvailability() == "Available":
            return("This book has not been checked out.")
        user = users.get(user_id, None)
        if user is None:
            return("User with this ID does not exist.")
        book.setAvailability("Available")
        user.deleteBorrowedBook(ISBN, book.getTitle())
        return(f"User {user_id} returned book {book.getTitle()}")
    except Exception as e:
        print(f"Error occurred: {e}")

def searchForBook(ISBN="", title=""):
    try:
        if ISBN == "" and title == "":
            return("You must enter at least the ISBN or book title to search.")
        if ISBN != "":
            book = books.get(ISBN, None)
            return f"""Book ISBN: {ISBN} \n Book title: {book.getTitle()} \n Book author: {book.getAuthor()} \n Book publication date: {book.getPublicationDate()} \n Book availability: {book.getAvailability()} \n Book genre: {book.getGenreName()}"""
        elif title != "":
            for book_details in books.values():
                if book_details.getTitle() == title:
                    return f"""Book ISBN: {book_details.getISBN()} \n Book title: {title} \n Book author: {book_details.getAuthor()} \n Book publication date: {book_details.getPublicationDate()} \n Book availability: {book_details.getAvailability()} \n Book genre: {book_details.getGenreName()}"""
        return("Book could not be found.")
    except Exception as e:
        print(f"Error occurred: {e}")

def displayAllBooks():
    try:
        for book_details in books.values():
            print(f"""Book ISBN: {book_details.getISBN()} \n Book title: {book_details.getTitle()} \n Book author: {book_details.getAuthor()} \n Book publication date: {book_details.getPublicationDate()} \n Book availability: {book_details.getAvailability()} \n Book genre: {book_details.getGenreName()}""")
    except Exception as e:
        print(f"Error occurred: {e}")

def addUser(name, id):
    try:
        new_user = User(name, id, {})
        users.update({id: new_user})
        print("Added new user!")
    except Exception as e:
        print(f"Error occurred: {e}")

def viewUserDetails(id):
    try:
        user = users.get(id, None)
        if user == None:
            print("Could not find user with this ID.")
        else:
            print(f"User ID: {id} \n    User name: {user.getUserName()}\n")
            print(" Borrowed books list:")
            for title in user.getBorrowedBooks().values():
                print(f"    {title}")
    except KeyError:
        print("Could not find user with this ID")
    except Exception as e:
        print(f"Error occurred: {e}")

def displayAllUsers():
    try:
        for user in users.values():
            print(f"User ID: {user.getID()} \n    User name: {user.getUserName()}\n")
            print(" Borrowed books list:")
            for title in user.getBorrowedBooks().values():
                print(f"    {title}")
            print("---------------------")
    except Exception as e:
        print(f"Error occurred: {e}")

def addAuthor(name, bio):
    try:
        new_author = Author(name, bio)
        authors.update({name: new_author})
        print("Added new author!")
    except Exception as e:
        print(f"Error occurred: {e}")

def viewAuthorDetails(name):
    try:
        author = authors.get(name, None)
        if author == None:
            print("Could not find author with this name.")
        else:
            print(f"Author name: {name} \n    Bio: {author.getBio()}\n")
    except Exception as e:
        print(f"Error occurred: {e}")

def displayAllAuthors():
    try:
        for author in authors.values():
            print(f"Author name: {author.getAuthorName()} \n    Bio: {author.getBio()}\n")
            print("---------------------")
    except Exception as e:
        print(f"Error occurred: {e}")

def addGenre(name, description, category):
    try:
        new_genre = Genre(name, description, category)
        genres.update({name: new_genre})
        print("Added new genre!")
    except Exception as e:
        print(f"Error occurred: {e}")

def viewGenreDetails(name):
    try:
        genre = genres.get(name, None)
        if genre == None:
            print("Could not find genre with this name.")
        else:
            print(f"Genre name: {name} \n    Genre description: {genre.getDescription()}\n  Genre category: {genre.getCategory()}")
    except Exception as e:
       print(f"Error occurred: {e}")

def displayAllGenres():
    try:
        for genre in genres.values():
            print(f"Genre name: {genre.getGenreName()} \n    Genre description: {genre.getDescription()}\n  Genre category: {genre.getCategory()}")
            print("---------------------")
    except Exception as e:
        print(f"Error occurred: {e}")
