import random

book_list = [ 
    "The lord is my sheperd",
    "What if him no be your helper",
    "oyo for you",
    "kill me",
    "you wan die keh",
    "i need gle",
    "God no go shame us",
    "it is well"
]

    

def main_menu():
    choice=0
    while choice != -1:
        print()
        print("Welcome to the book suggestion system!")
        print("1. Get Suggestions")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Update Book")
        print("5. Show all books")
        print("-1. Quit")
        choice = input("Select an option: ")
 
        
        if choice == '1':
            #name_of_book = input("Book of the day:")
            second_option = "y"
            while second_option == 'y':
                print("Book for the Day")
                book = get_Suggestions()
                print("Book Title: "+book)
                print("Page: ", get_book_page(book))
               # print(book_list)
                second_option = input("Enter Y if you want another suggesstion or enter any word to continue ")
                

        if choice == '2':
            name_of_book = input("Kindly enter the name of the book:")
            print(addBook(name_of_book))

        elif choice == '3':
            name_of_book = input("Kindly enter the name of the book you want to remove:")
            print(remove_book(name_of_book))

        elif choice == '4':
            name_of_book = input("Enter the old title:")
            new_title = input("Enter the new title:")
            print(update_book(name_of_book, new_title))

        elif choice == '5':
            show_all_books()

        elif choice == '-1':
            print("bye bro")
            break

        else:
            print("Wrong input, try again")
            main_menu()


  
    
def get_Suggestions():
    get_Suggestions = random.choice(book_list)
    return get_Suggestions

def get_book_page(book):
    for count in range(len(book_list)):
        if book == book_list[count]:
            return count+1
    
       

def addBook(name):
    book_list.append(name)
    return "Book added successfully"

def remove_book(name): 
    book_list.remove(name)
    #print(book_list)
    return "Book removed succesffully"

def update_book(name_of_book, new_title):
    for book in book_list:
        if book.lower() == name_of_book.lower():
            book_list.remove(book)
            book_list.append(new_title)
            return "Book updated successfully!"
    return "Old Book not found"

def show_all_books():
    if book_list == []:
        return "The book list is empty"
    else:
        for book in book_list:
            print(book)
     
main_menu()






        
