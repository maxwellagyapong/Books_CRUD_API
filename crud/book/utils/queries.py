import csv
import random
from ..models import Book
from ..serializers import BookSerializer
from .script_runner import run_command


#Make migrations
def perform_makemigrations():
    command_to_run = 'python manage.py makemigrations book'
    run_command(command_to_run)

#Finally migrate
def perform_migrate():
    command_to_run = 'python manage.py migrate'
    run_command(command_to_run)

#Create Books Table in PostgreSQL
def perform_migrations():
    perform_makemigrations()
    perform_migrate()

#Insert 5 books into the table
def insert_books():

    with open(r'C:\Users\maxwe\OneDrive\Desktop\Projects\Book Project\crud\book\utils\books.csv', "r", encoding='utf-8') as file:
        book_data = csv.reader(file)

        next(book_data)

        book_data_list = []
        for id_, row in enumerate(book_data):
            (
                title,
                author,
                year,
            ) = row
            book_data_list.append(
                Book(
                title=title,
                author=author,
                year=year,
                )
            )
    # Make a book bulk create
    Book.objects.bulk_create(book_data_list)

#Retrieve all books from db and print to console
def retrieve_all_books():
    books = Book.objects.all()
    print("Title | Author | Year")
    print("----------------------")
    for book in books:
        print(f"{book.title} | {book.author} | {book.year}")
    print("")

#Update Year of one book
def update_year():
    print("Updating the year of any random book...\n")
    book_id = random.randint(1, 5) 
    book = Book.objects.get(id=book_id)
    new_year = 2023

    new_data = ({"title": book.title, "author": book.author, "year": new_year})
    serializer = BookSerializer(book, data=new_data)
    if serializer.is_valid():
        serializer.save()
    else:
        raise ValueError("Wrong, year! Book can't be updated.")

    print(f"Year of book with id {book_id} has been updated!")
    retrieve_all_books()

#Delete one book
def delete_book():
    print("Deleting any random book...\n")
    book_id = random.randint(1, 5)
    book = Book.objects.get(id=book_id)
    book.delete()

    print(f"Book with id {book_id} has been deleted!")
    retrieve_all_books()
