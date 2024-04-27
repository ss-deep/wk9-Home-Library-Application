### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def add_new_book():
#     title=input("Enter book name : ")
#     author=input("Enter author of that book : ")
#     year=input("Enter year of publishing : ")
#     rating=input("Enter rating for book : ")
#     pages=input("Enter total pages in the book : ")
#     book={
#         'title':title,
#         'author':author,
#         'year':year,
#         'rating':rating,
#         'pages':pages
#     }
#     return book

# add_new_book()

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out 
# your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def add_new_book():
#     title=input("Enter book name : ")
#     author=input("Enter author of that book : ")
#     year=int(input("Enter year of publishing : "))
#     rating=float(input("Enter rating for book : "))
#     pages=int(input("Enter total pages in the book : "))
#     book={
#         'title':title,
#         'author':author,
#         'year':year,
#         'rating':rating,
#         'pages':pages
#     }
#     return book

# add_new_book()




### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def add_new_book():
    title=input("\n\nEnter book name : ")
    author=input("Enter author of that book : ")
    while True:
        try:
            year=int(input("Enter year of publishing : "))
            rating=float(input("Enter rating for book : "))
            pages=int(input("Enter total pages in the book : "))
        except:
            print("\nPlease provide valid input:\n")
            continue
        else:
            book={
                'title':title,
                'author':author,
                'year':year,
                'rating':rating,
                'pages':pages
            }
            print('\n\nBook added to the library.\n')
            break
        book_library.append(book)
            

# add_new_book()


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# def main_menu():
#     print("Pick one from the options:\n 1:Add new book\n 2:Search book\n 3:Show all the books\n")
#     while True:
#         try:
#             choice=int(input("Enter your choice : "))
#         except:
#             print("Please pick one from 1, 2 and 3 ")
#             continue
#         else:
#             if choice==1:
#                 add_new_book()
#             elif choice==2:
#                 print("Coming soon....")
#             else:
#                 print("Here are all the books... \n")
#         finally:
#             print("Great choice!")


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the 
# program. Call the main menu to ensure it functions properly.

# Code here
book_library = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.5,
        "pages": 309
    },
    {
        "title": "Twilight",
        "author": "Stephenie Meyer",
        "year": 2005,
        "rating": 3.6,
        "pages": 498
    },
    {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "year": 2012,
        "rating": 4.2,
        "pages": 313
    },
    {
        "title": "Divergent",
        "author": "Veronica Roth",
        "year": 2011,
        "rating": 4.2,
        "pages": 487
    },
    {
        "title": "Mockingjay",
        "author": "Suzanne Collins",
        "year": 2010,
        "rating": 4.06,
        "pages": 398
    }   
]

def search_book():
    book_name=input("\n\nEnter book name you want to search : ")
    for book in book_library:
        if book_name==book['title']:
            return print_book([book])
    print(f"\n\nThe book '{book_name}' not available in the library.")
        
def print_book(book_list):
    for book in book_list:
        print(f" \nBook Title : {book['title']}\n Author : {book['author']}\n Year : {book['year']}\n Rating : {book['rating']}\n Pages : {book['pages']}")

def main_menu():
    while True:
        try:
            print("\n\nPick one from the options:\n 1:Add new book\n 2:Search book\n 3:Show all the books\n 4:Exit\n")
            choice=int(input("Enter your choice : "))
        except:
            print("\nPlease pick one from 1, 2, 3 or 4")
            continue
        else:
            if choice==1:
                add_new_book()
            elif choice==2:
                search_book()
            elif choice==3:
                print("\nHere are all the books... \n")
                print_book(book_library)
            elif choice==4:
                print('\n Have a great day!')
                break

main_menu()