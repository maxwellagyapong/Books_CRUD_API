# Python/django imports
from django.test import TestCase
from django.urls import reverse, resolve

# Local apps imports
from book import views
from book.models import Book

""" App urls/routes test class"""
class TestUrls(TestCase):
    def test_book_list_route(self):
        url = reverse("home")
        url_view_function = resolve(url).func
        self.assertEqual(url_view_function, views.book_list)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.book = Book.objects.create(
            title="Test Book Title",
            author="Test Book Author",
            year="2023-07-19",
        )

    def test_book_detail_route(self):
        url = reverse("detail", args=(self.book.id,))
        url_view_function = resolve(url).func
        self.assertEqual(url_view_function, views.book_detail)
