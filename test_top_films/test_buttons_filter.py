import allure
import datetime
from common import BaseTest
from pages.top_films import TopFilms


class TestMain(BaseTest):
    date = datetime.datetime.now()

    def setup(self):
        self.top_films = TopFilms(driver=self.driver, url="https://www.kinopoisk.ru/lists/movies/top250/")

    @allure.title("Переходим на страницу топ 250")
    def test_01_guest_can_go_to_login_page(self):
        with allure.step("Переходим на страницу топ 250"):
            self.top_films.go_to_site()
            self.top_films.check_load_page()
            self.top_films.drop_filters.select_filter("Все жанры", "Боевики")

    @allure.title("Переходим на страницу топ 250")
    def test_02_guest_can_go_to_login_page_2(self):
        with allure.step("Переходим на страницу топ 250"):
            self.top_films.go_to_site()
            self.top_films.check_load_page()
            self.top_films.filters.select_filter("Российские")
