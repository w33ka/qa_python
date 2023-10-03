import pytest
from main import BooksCollector


@pytest.fixture
def book_collector():
    return BooksCollector()
