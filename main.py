import libraryInterface

def main():
    try:
        while True:
            print("""Welcome to the Library Management System!

                    Main Menu:
                    1. Book Operations
                    2. User Operations
                    3. Author Operations
                    4. Genre Operations
                    5. Quit
            """)
            operation_category = int(input("Enter the number (1-5):"))
            if operation_category == 5:
                break
            elif operation_category == 1:
                libraryInterface.book_operations()
            elif operation_category == 2:
                libraryInterface.user_operations()
            elif operation_category == 3:
                libraryInterface.author_operations()
            elif operation_category == 4:
                libraryInterface.genre_operations()
            else:
                raise Exception
    except (ValueError, TypeError):
      print("Error! Remember, enter an integer between 1-5 as an option.")
    except Exception as e:
        print(e)
    finally:
        print("Thank you for using the library management system!")
if __name__ == "__main__":
    main()