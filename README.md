# qa_python
# СПИСОК ПРОВЕРОК

# test_add_new_book_without_genre
Реализована проверка добавления книги без жанра

# test_add_new_book_without_genre_more_than_40symbols
Реализована проверка добавления книги с названием более 40 символов

# test_set_book_genre
Реализована проверка добавления книги с жанром

# test_get_books_with_specific_genre
Реализована проверка получения списка книг по выбранному жанру

# test_get_books_for_children
Реализована проверка получения книг подходящих для детей

# test_add_book_in_favorites
Реализована проверка добавления книг в список "Избранные"

# test_add_book_in_favorites_re_adding_negativ
Реализована проверка добавления книг в список "Избранные" повторно

# test_add_book_in_favorites_book_not_in_books_genre
Реализована проверка добавления книги которой нет в списке книг

# test_delete_book_from_favorites 
Реализована проверка удаления книги из списка "Избранные"

# Запуск
Для запуска тестов необходимо написать команду в терминале :
pytest -v tests.py 
где -v обозначает подробный вывод результатов
