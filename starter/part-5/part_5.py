### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and 
# call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def add_new_book():
    title=input("Enter book name : ")
    author=input("Enter author of the book : ")
    while True:
        try:
            year=int(input("Enter year of publishing : "))
            rating=float(input("Enter rating for book : "))
            pages=int(input("Enter total pages in the book : "))
        except:
            print("Please provide valid input:")
            continue
        else:
            break
    
    with open("book_library.txt", "a") as book_info:
        book_info.write(f"{title}, {author}, {year}, {rating}, {pages}\n")




### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by 
# reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def get_book_data():
    with open("book_library.txt", "r") as book_info:
        lines = book_info.readlines()
    book_list=[]
    for line in lines:
        title, author, year, rating, pages = line.split(", ")
        book_list.append({'title':title, 'author':author, 'year':year, 'rating':rating, 'pages':pages})
    return book_list
### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a 
# module elsewhere.

# Code this at the bottom of the script
# if __name__=='__main__':
#     main_menu()


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your 
# first Python application finished!


def search_book():
    all_books=get_book_data()
    book_name=input("\n\nEnter book name you want to search : ")
    for book in all_books:
        if book_name==book['title']:
            return print_book([book])
    print(f"\n\nThe book '{book_name}' not available in the library.")
        
def print_book(book_list):
    for book in book_list:
        print(f" Book Title : {book['title']}\n Author : {book['author']}\n Year : {book['year']}\n Rating : {book['rating']}\n Pages : {book['pages']}")

def total_books(book_list):
    print(f'There are total {len(book_list)} books in the library.')

def top_rated_book(book_list):
    rating=0
    max_rated_book={}
    for book in book_list:
        if(rating<float(book['rating'])):
            rating=float(book['rating'])
            max_rated_book=book
    print_book([max_rated_book])

def main_menu():
    all_books=get_book_data()
    while True:
        try:
            print("\n\nPick one from the options:\n 1:Add new book\n 2:Search book\n 3:Show all the books\n 4:Find total books in the library\n 5:Top rated book\n 6:Exit \n")
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
                print_book(all_books)
            elif choice==4:
                print("\nHere are all the books... \n")
                total_books(all_books)
            elif choice==5:
                print("\nThe top rated book is... \n")
                top_rated_book(all_books)
            elif choice==6:
                print('\n Have a great day!')
                break


if __name__=='__main__':
    main_menu()
