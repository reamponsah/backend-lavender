print("Welcome to the Book Title Library!")
menu = "Please choose an option from the list below: \n1. Add a book\n2. Remove a book\n3. View all books\n4. Exit"

books = []

while True:
    print(menu)
    option = input("Enter an option(1-4): ")
    
    
    if option == "1":
        add_books = input("What book do you want to add?: ").split(', ')
        books.extend(add_books)
        print("Book(s) succesfully added!")
        print(books)

        
    elif option == "2":
        rem_book = input("What book do you want to remove?: ")
        if rem_book in books:
            books.remove(rem_book)
            print(f"'{rem_book}' succesfully removed!")

        else:
            print("Invalid Entry. Book Not Found")
            

    elif option == "3":
        print(f"Books in library: {books}")     

    elif option == "4":
        print("Exiting Library...")       
        break

    else:
        print("Invalid Option! Try again")