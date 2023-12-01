import allure
import datetime
from pages.top_films import TopFilms


class TestMain:
    date = datetime.datetime.now()

    @allure.title("Переходим на страницу топ 250")
    def test_guest_can_go_to_login_page(self, browser):
        self.top_films = TopFilms(driver=browser,
                                   url="https://www.kinopoisk.ru/lists/movies/top250/")

        with allure.step("Переходим на страницу топ 250"):
            self.top_films.go_to_site()
            self.top_films.check_load_page()
            self.top_films.filters.select_filter("Фильмы")
