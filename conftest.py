import pytest
from main import BooksCollector


@pytest.fixture
def book_collector():
    return BooksCollector()


def pytest_make_parametrize_id(config, val):
    return repr(val)