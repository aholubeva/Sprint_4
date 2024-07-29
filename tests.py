import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['О', 'Война и мир', 'Война и мир и много много много из мир40'])
    def test_add_new_book_with_valid_symbols_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert name in list(collector.books_genre)

    @pytest.mark.parametrize('name', ['', 'Война и мир и много много много мир мир41'])
    def test_add_new_book_with_invalid_symbols_length(self, name):

        collector = BooksCollector()
        collector.add_new_book(name)

        assert name not in list(collector.books_genre)

    def test_add_new_book_with_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')

        assert collector.books_genre['Книга1'] == ''

    def test_set_book_genre_and_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.set_book_genre('Идиот', 'Ужасы')

        assert collector.get_book_genre('Идиот') == 'Ужасы'


    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Рапунцель')
        collector.set_book_genre('Рапунцель', 'Мультфильмы')
        collector.add_new_book('Моана')
        collector.set_book_genre('Моана', 'Мультфильмы')

        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 2 and collector.get_books_with_specific_genre('Мультфильмы') == ['Рапунцель', 'Моана']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Немо')
        collector.set_book_genre('Немо', 'Мультфильмы')
        collector.add_new_book('Золушка')
        collector.set_book_genre('Золушка', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Немо', 'Золушка']

    def test_get_books_for_children_should_be_without_books_from_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Морозко')
        collector.set_book_genre('Морозко', 'Мультфильмы')

        assert len(collector.get_books_for_children()) == 1 and collector.get_books_for_children() == ['Морозко']


    def test_add_book_in_favorites_can_be_added_just_one_time(self):
        collector = BooksCollector()
        collector.add_new_book('Люди на болоте')
        collector.add_new_book('Павлинка')
        collector.add_book_in_favorites('Павлинка')
        collector.add_book_in_favorites('Павлинка')

        assert len(collector.get_list_of_favorites_books()) == 1 and collector.get_list_of_favorites_books() == ['Павлинка']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Три сестры')
        collector.add_new_book('Корона')
        collector.add_book_in_favorites('Корона')
        collector.add_book_in_favorites('Три сестры')
        collector.delete_book_from_favorites('Корона')

        assert len(collector.get_list_of_favorites_books()) == 1 and collector.get_list_of_favorites_books() == ['Три сестры']



