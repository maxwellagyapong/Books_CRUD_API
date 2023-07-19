# Python/django imports
from django.test import TestCase

# Local apps imports
from book.models import Book

""" App models test class"""
class TestModels(TestCase):
    def test_loan_model_fields(self):
        # Create required model instances for test
        book = Book.objects.create(
            title="Harry Porter",
            author = "Mary",
            year = "1994-09-12"
        )
        # Assertions
        self.assertTrue(Book.objects.filter(id=book.id).exists())

