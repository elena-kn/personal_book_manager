from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os


load_dotenv()

name = input("enter your name: ")
print("welcom", name)
admin_mode = input("do you want to enter admin mode(yes / no)? ")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password == os.getenv("admin_pass"):
        print("adminmod actited")
    else:
        print("wrong password") 
books = load_books()
count_books = int(input("how many books do you eant to add ? ")) 
for i in range(count_books):
    book  = input("enter a books: ")
    books.append(book)
show_books(books)
save_books(books)