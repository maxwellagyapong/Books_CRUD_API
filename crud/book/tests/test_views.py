# Python/django imports
from django.test import TestCase
from django.urls import reverse

# Local apps imports
from book.models import Book

""" App urls/routes test class"""
class TestViews(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.book = Book.objects.create(
            title="Test Book Title",
            author="Test Book Author",
            year="2023-07-19",
        )

    def test_book_list_view(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view(self):
        url = reverse("detail", args=(self.book.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
