import unittest
from src.library import Library, BookAlreadyExistsError

class TestLibrarySprint1(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        result = self.library.add_book(book_id=1, title="Book A", author="Author A")
        self.assertTrue(result)
        self.assertIn(1, self.library.books)

    def test_add_duplicate_book_raises_error(self):
        self.library.add_book(book_id=1, title="Book A", author="Author A")
        with self.assertRaises(BookAlreadyExistsError):
            self.library.add_book(book_id=1, title="Book B", author="Author B")

