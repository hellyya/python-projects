#list of dictionaries
library = [{"title": "untamed", "author": "glen", "status": "available"},
           {"title": "bell jar", "author": "sylvia plath", "status": "available"},
           {"title": "nadja", "author": "andre breton", "status": "borrowed"},
           {"title": "dora", "author": "froyd", "status": "available"}]

def display_available_books():
    print("available books")
    available_found = False
    for book in library:
        if book["status"]== "available":
            print(f"'{book['title']}' by {book['author']}")
            available_found = True
    if not available_found:
        print("none of the books are available.")

display_available_books()

request= input("enter the title of the book you want to borrow:").strip()

found = False
for book in library:
    if book["title"].lower() == request.lower():
        found = True
        if book["status"] == "available":
            book["status"] = "borrowed"
            print("you have borrowed '{book['title']}'.")
        else:
            print("sorry, '{book['title']}' is unavailable.") 
        break
if not found:
    print("error, this book does not exisst.")

return_request= input("enter the title of the book to return: ").strip()
found = False
for book in library:
    if book["title"].lower() == return_request.lower():
        found = True
    if book["status"]=="borrowed":
        book["status"]= "avilable"
        print("youve returned '{book['title']}'.")
    else:
        print("this book was already available.")
    break

if not found:
    print("error, book not found.")

display_available_books()