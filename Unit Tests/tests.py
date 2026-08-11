import pytest
from main import BooksCollector


class TestBooksCollector:

    
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')

        assert len(collector.books_genre) == 2

    
    def test_add_new_book_not_add_book_with_long_name(self):
        collector = BooksCollector()

        collector.add_new_book('Очень длинное название книги которое больше сорока символов')

        assert len(collector.books_genre) == 0

    
    def test_add_new_book_has_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('1984')

        assert collector.books_genre['1984'] == ''

    
    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Оно', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы'),
            ('Марсианин', 'Фантастика')
        ]
    )
    def test_set_book_genre_set_valid_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)

        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    # Проверка получения жанра книги
    def test_get_book_genre_return_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    
    def test_get_books_with_specific_genre_return_books(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок', 'Детективы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    
    def test_get_books_genre_return_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')

        expected_result = {'Дюна': ''}

        assert collector.get_books_genre() == expected_result

    
    def test_get_books_for_children_return_book_without_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Мадагаскар')
        collector.set_book_genre('Мадагаскар', 'Мультфильмы')

        books_for_children = collector.get_books_for_children()

        assert 'Мадагаскар' in books_for_children


    def test_get_books_for_children_not_return_book_with_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        books_for_children = collector.get_books_for_children()

        assert 'Оно' not in books_for_children

    
    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Дюна')

        assert 'Дюна' in collector.get_list_of_favorites_books()

    
    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        collector.delete_book_from_favorites('Дюна')

        assert 'Дюна' not in collector.get_list_of_favorites_books()

    