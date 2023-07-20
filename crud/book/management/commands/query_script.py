from django.core.management import BaseCommand
from book.utils.queries import perform_migrations, insert_books, retrieve_all_books, update_year, delete_book

"""Script responsible for performing sample CREATE, RETRIEVE, UPDATE, DELETE, etc"""

class Command(BaseCommand):
    help = "Runs a Selenium script to scrape data from a website"

    def handle(self, *args, **options):
        perform_migrations()
        insert_books()
        retrieve_all_books()
        update_year()
        delete_book()
