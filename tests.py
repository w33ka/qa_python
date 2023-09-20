import pytest


#проверка на добавление книги без жанра и получение текщего словаря books_genre
def test_add_new_book_without_genre(book_collector):
    book_collector.add_new_book('Гарри Поттер')
    book_collector.add_new_book('Властелин Колец')

    result = book_collector.get_books_genre()
    assert len(result) != 0


#проверка на добавление книги с названием больше 40 символов
def test_add_new_book_without_genre_more_than_40symbols(book_collector):
    book_collector.add_new_book('БольшаяКнигаНастолькоЧтоНеУмещаетсяСюдаОй')

    result = book_collector.get_books_genre()
    assert 'БольшаяКнигаНастолькоЧтоНеУмещаетсяСюдаОй' not in result


#добавление книги с жанром который есть в списке genre и проверка жанра книги по имени
def test_set_book_genre(book_collector):
    book_collector.add_new_book('Гарри Поттер')
    book_collector.set_book_genre('Гарри Поттер', 'Фантастика')
    assert book_collector.get_book_genre('Гарри Поттер') == 'Фантастика'


#проверка списка книг по выбранному жанру

def test_get_books_with_specific_genre(book_collector):
    book_collector.add_new_book('Гарри Поттер')
    book_collector.add_new_book('Властелин Колец')
    book_collector.add_new_book('Тупой и еще тупее')

    book_collector.set_book_genre('Гарри Поттер', 'Фантастика')
    book_collector.set_book_genre('Властелин Колец', 'Фантастика')
    book_collector.set_book_genre('Тупой и еще тупее', 'Комедии')

    result = book_collector.get_books_with_specific_genre('Фантастика')
    assert result == ['Гарри Поттер', 'Властелин Колец']


#проверка на книги для детей должны быть только с жанром без возрастного рейтинга.
def test_get_books_for_children(book_collector):
    book_collector.add_new_book('Красная шапочка')
    book_collector.add_new_book('Колобок')

    book_collector.set_book_genre('Красная шапочка', 'Мультфильмы')
    book_collector.set_book_genre('Колобок', 'Детектив')

    children_book = book_collector.get_books_for_children()
    assert 'Красная шапочка' in children_book and 'Колобок' not in children_book

# проверка на добавление книги в избранное из словаря books_genre  и проверка на вывод списка избранного
@pytest.mark.parametrize('book_name', ['Винни Пух', 'Буратино'])
def test_add_book_in_favorites(book_collector,book_name):
    book_collector.add_new_book(book_name)
    book_collector.add_book_in_favorites(book_name)

    favorites = book_collector.get_list_of_favorites_books()
    assert book_name in favorites

# проверка на добавление книги повторно
def test_add_book_in_favorites_re_adding_negativ(book_collector):
    book_collector.add_new_book('Винни Пух')
    book_collector.add_book_in_favorites('Винни Пух')

    favorites = book_collector.get_list_of_favorites_books()
    assert 'Винни Пух' in favorites

    book_collector.add_book_in_favorites('Винни Пух')
    favorites = book_collector.get_list_of_favorites_books()
    assert favorites.count('Винни Пух') == 1

# проверка на добавление книги которой нет в списке books_genre
def test_add_book_in_favorites_book_not_in_books_genre(book_collector):
    book_collector.add_book_in_favorites('Война и  Мир')
    favorites = book_collector.get_list_of_favorites_books()
    assert 'Война и Мир' not in favorites

#проверка на удаление книги из избранного
def test_delete_book_from_favorites(book_collector):
    book_collector.add_new_book('Белоснежка и семь гномов')
    book_collector.add_new_book('Маленький принц')
    book_collector.add_book_in_favorites('Белоснежка и семь гномов')
    book_collector.add_book_in_favorites('Маленький принц')
    book_collector.delete_book_from_favorites('Белоснежка и семь гномов')

    favorites = book_collector.get_list_of_favorites_books()
    assert 'Белоснежка и семь гномов' not in favorites
