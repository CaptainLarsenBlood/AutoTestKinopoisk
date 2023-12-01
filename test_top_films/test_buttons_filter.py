import allure
import datetime
import pytest
from common import BaseTest
from pages.top_films import TopFilms


def read_eth_data():
    films_eth = []
    with open('test-files/films_eth.txt', "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            films_eth.append((line[:line.find(',')], line[line.find(',') + 1:],))

        return films_eth


class TestMain(BaseTest):
    date = datetime.datetime.now()
    films_eth = read_eth_data()

    def setup(self):
        self.top_films = TopFilms(self.driver, "https://www.kinopoisk.ru/lists/movies/top250/")

        with allure.step("Переходим на страницу топ 250"):
            self.top_films.go_to_site()
            self.top_films.check_load_page()

    @pytest.mark.parametrize("type_filter,list_films", films_eth)
    def test_01_check_button_filters(self, type_filter, list_films):
        """Проверяем кнопочные фильтры"""

        with allure.step(f"Выбираем фильтр {type_filter} и проверяем список фильмов"):
            self.top_films.filters.select_filter(type_filter)
            for film in self.top_films.get_films():
                assert film in list_films, f"Фильма {film} нет в списке"