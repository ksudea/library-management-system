# Module for user interface, input validation, and interaction with library manager through operation choices

import libraryManager
import validation_handler as vh


def book_operations():
  try:
    while True:
            print("""Book Operations:
                        1. Add a new book
                        2. Borrow a book
                        3. Return a book
                        4. Search for a book
                        5. Display all books
                        6. Return to main menu
            """)
            operation = int(input("Enter the number (1-6):"))
            if operation == 1:
              try:
                while True: 
                    book_title = input("Enter valid book title: ")
                    if not vh.book_title_validate(book_title):
                        raise Exception
                    book_author = input("Book author: ")
                    if not vh.name_validate(book_author):
                        raise Exception
                    print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                    book_isbn = input("Book ISBN: ")
                    if not vh.book_ISBN_validate(book_isbn):
                        raise Exception
                    book_publication_date = input("Book publication date: ")
                    if not vh.book_publication_date_validate(book_publication_date):
                        raise Exception
                    book_genre = input("Book genre (press enter to skip): ")
                    if not book_genre == "" and not vh.name_validate(book_genre):
                        raise Exception
                    book_genre_description = input("Book genre description(press enter to skip): ")
                    book_genre_category = input("Book genre category(press enter to skip): ")
                    libraryManager.addBook(book_title, book_author, book_isbn, book_publication_date, book_genre, book_genre_description, book_genre_category)
                    break
              except Exception as e:
                  print(f"Invalid input! Try again.")
            elif operation == 2:
                print("You need both User ID and Book ISBN to borrow.")
                try:
                    user_id = input("Library user ID: ")
                    if vh.user_id_validate(user_id):
                        print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                        book_isbn = input("Library book ISBN: ")
                        if vh.book_ISBN_validate(book_isbn):
                            print(libraryManager.borrowBook(user_id, book_isbn))
                            break
                        else: 
                            print("Invalid book ISBN.")
                    else:
                        print("Invalid user ID.")
                except Exception as e:
                    print(f"Error! Check input. {e}")
            elif operation == 3: 
                print("You need both User ID and Book ISBN to return.")
                try:
                    user_id = input("Library user ID: ")
                    if vh.user_id_validate(user_id):
                        print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                        book_isbn = input("Library book ISBN: ")
                        if vh.book_ISBN_validate(book_isbn):
                            print(libraryManager.returnBook(user_id, book_isbn))
                            break
                        else: 
                            print("Invalid book ISBN.")
                    else:
                        print("Invalid user ID.")
                except Exception as e:
                    print(f"Error! Check input. {e}")
            elif operation == 4:
                print("You need either ISBN or book title or both to search.")
                try:
                    print("Enter a valid ISBN-13 number (format: XXX-X-XXXX-XXXX-X or XXX X XXXX XXXX X or without spaces).")
                    book_isbn = input("Book ISBN(press enter to skip): ")
                    if book_isbn == "" or vh.book_ISBN_validate(book_isbn):
                        book_title = input("Library book title(press enter to skip): ")
                        if book_title == "" or vh.book_title_validate(book_title):
                            print(libraryManager.searchForBook(book_isbn, book_title))
                            break
                        else: 
                            print("Invalid book title.")
                    else:
                        print("Invalid book ISBN.")
                except Exception as e:
                    print(f"Error! Check input. {e}")
            elif operation == 5: 
                libraryManager.displayAllBooks()
            elif operation == 6:
                break
            else:
                print("Incorrect input. Try again")
  except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-6 as an option.")
  except Exception as e:
      print(f"Error in book operations: {e}")

def user_operations():
    try:
        while True:
            print("""User Operations:
                        1. Add a new user
                        2. View user details
                        3. Display all users
                        4. Return to main menu
            """)
            operation = int(input("Enter the number (1-4):"))
            if operation == 1:
                user_name = input("Valid user name: ")
                if vh.name_validate(user_name):
                    user_id = input("Library user ID: ")
                    if vh.user_id_validate(user_id):
                        libraryManager.addUser(user_name,user_id)
                    else:
                        print("Input valid user ID.")
                else:
                        print("Input valid user name.")
            elif operation == 2:
                user_id = input("Library user ID: ")
                if vh.user_id_validate(user_id):
                    libraryManager.viewUserDetails(user_id)
                else:
                    print("Input valid user ID to view user details")
            elif operation == 3:
                libraryManager.displayAllUsers()
            elif operation == 4:
                break
    except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-4 as an option.")
    except Exception as e:
        print(e)

def author_operations():
    try:
        while True:
            print("""Author Operations:
                        1. Add a new author
                        2. View author details
                        3. Display all authors
                        4. Return to main menu
            """)
            operation = int(input("Enter the number (1-4):"))
            if operation == 1:
                author_name = input("Enter valid author name: ")
                if vh.name_validate(author_name):
                    author_bio = input("Author bio(press enter to skip): ")
                    libraryManager.addAuthor(author_name, author_bio)
                else:
                    print("Invalid title input. Try again")
            elif operation == 2: 
                author_name = input("Author name: ")
                if vh.name_validate(author_name):
                    libraryManager.viewAuthorDetails(author_name)
                else:
                    print("Input valid user ID to view user details")
            elif operation == 3:
                libraryManager.displayAllAuthors()
            elif operation == 4:
                break
    except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-4 as an option.")
    except Exception as e:
        print(e)

def genre_operations():
    try:
        while True:
            print("""Genre Operations:
                        1. Add a new genre
                        2. View genre details
                        3. Display all genres
                        4. Return to main menu
            """)
            operation = int(input("Enter the number (1-4):"))
            if operation == 1:
                genre_name = input("Enter valid genre name: ")
                if vh.name_validate(genre_name):
                    genre_description = input("Genre description(press enter to skip): ")
                    genre_category = input("Genre category (press enter to skip)")
                    libraryManager.addGenre(genre_name, genre_description, genre_category)
                else:
                    print("Invalid genre name input. Try again")
            elif operation == 2: 
                genre_name = input("Genre name: ")
                if vh.name_validate(genre_name):
                    libraryManager.viewGenreDetails(genre_name)
                else:
                    print("Input valid genre name to view details")
            elif operation == 3:
                libraryManager.displayAllGenres()
            elif operation == 4:
                break
    except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-4 as an option.")
    except Exception as e:
        print(e)