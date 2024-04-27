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

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary 
# as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_details(book):
    print( f"The name of the book is {book['title']}. The author is {book['author']}. It was published in {book['year']} and its rating is {book['rating']}. There are total pages {book['pages']} in the book.")

book_details(book_library[0])

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_author(book):
    return book['author']

def book_year(book):
    return book['year']

def book_rating(book):
    return book['rating']

def book_pages(book):
    return book['pages']


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you 
# could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def total_books(book_list):
    print(f'There are total {len(book_list)} books in the library.')

def total_pages(book_list):
    total_pages=0
    for book in book_list:
        total_pages+=book['pages']
    return total_pages

def get_authors(book_list):
    all_authors=set()
    for book in book_list:
        all_authors.add(book['author'])
    return all_authors

total_books(book_library)
print(f'List of available authors : {get_authors(book_library)}')
print(f'Total pages of all book : {total_pages(book_library)}')