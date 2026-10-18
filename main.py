from books import show_books, save_books, load_books

name = input("enter your name: ")
print("welcom", name)
books = load_books()
count_books = int(input("how many books do you eant to add ? ")) 
for i in range(count_books):
    book  = input("enter a books: ")
    books.append(book)
show_books(books)
save_books(books)