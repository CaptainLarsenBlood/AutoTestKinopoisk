import allure
import datetime
import pytest
from common import BaseTest
from pages.top_films import TopFilms


def read_eth_data(path):
    films_eth = []
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            films_eth.append((line[:line.find(',')], line[line.find(',') + 1:],))

        return films_eth


buttons_eth = read_eth_data('test-files/films_eth_1.txt')
dropdown_filter = read_eth_data('test-files/films_eth_2.txt')
combination_dropdown = read_eth_data('test-files/films_eth_3.txt')


class TestFilter(BaseTest):

    def setup(self):
        self.top_films = TopFilms(self.driver, "https://www.kinopoisk.ru/lists/movies/top250/")

        with allure.step("Переходим на страницу топ 250"):
            self.top_films.go_to_site()
            self.top_films.check_load_page()

    @pytest.mark.parametrize("type_filter,list_films", buttons_eth)
    def test_01_check_button_filters(self, type_filter, list_films):
        """Проверяем кнопочные фильтры"""

        with allure.step(f"Выбираем фильтр {type_filter} и проверяем список фильмов"):
            self.top_films.filters.select_filter(type_filter)
            for film in self.top_films.get_films():
                assert film in list_films, f"Фильма {film} нет в списке"

    @pytest.mark.parametrize("type_filter,list_films", dropdown_filter)
    def test_02_check_dropdown_filters(self, type_filter, list_films):
        """Проверяем выпадающие фильтры"""

        with allure.step(f"Выбираем фильтр {type_filter} и проверяем список фильмов"):
            self.top_films.drop_filters.select_filter(*type_filter.split(':'))
            for film in self.top_films.get_films():
                assert film in list_films, f"Фильма {film} нет в списке"

    @pytest.mark.parametrize("type_filters,list_films", combination_dropdown)
    def test_03_combination_dropdown_filters(self, type_filters, list_films):
        """Проверяем комбинацию выпадающих фильтров"""

        country, genre = type_filters.split()

        with allure.step(f"Выбираем страну - {country}, жанр {genre} и проверяем список фильмов"):
            self.top_films.drop_filters.select_filter("Все страны", country)
            self.top_films.drop_filters.select_filter("Все жанры", genre)
            for film in self.top_films.get_films():
                assert film in list_films, f"Фильма {film} нет в списке"
