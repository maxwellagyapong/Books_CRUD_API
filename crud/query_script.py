from book.models import Book

"""Script responsible for performing sample CREATE, RETRIEVE, UPDATE, DELETE, etc"""

#Create Books Table in PostgreSQL
def perform_migrations():
    pass

#Insert 5 books into the table
def insert_books():
    # # Make a book bulk create
    # Book.objects.bulk_create(book_data_model_list)
    pass

#Retrieve all books from db and print to console
def retrieve_all_books():
    pass

#Update Year of one book
def update_year():
    retrieve_all_books()
    pass

#Delete one book
def delete_book():
    retrieve_all_books()
    pass
