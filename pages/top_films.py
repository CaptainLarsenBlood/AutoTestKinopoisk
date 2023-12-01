from pages.base_page import BasePage
from elements.basic_elements import Element
from selenium.webdriver.common.by import By
from elements.filter import ButtonFilterList, DropDownFilterList


class TopFilms(BasePage):
    """PO для страниц с топ фильмами"""

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.filters = ButtonFilterList(self.driver, By.CSS_SELECTOR, ".styles_root__omMgy", rus_name="Фильтры кнопки")
        self.drop_filters = DropDownFilterList(self.driver, By.CSS_SELECTOR, '.styles_selectButton__4xHt7', rus_name="Выпадающие фильтры")
        self.advertising = Element(self.driver, By.CSS_SELECTOR, '.styles_container__XXCpX ', rus_name="Реклама")
        self.list_film = Element(self.driver, By.CSS_SELECTOR, ".styles_mainTitle__IFQyZ", rus_name="Список фильмов")

    def check_button_filters(self, filters: list):
        """Проверка, что кнопочные фильтры присутствуют на странице"""

        for i in filters:
            assert i in self.filters.filter_dict, f"фильтр {i} не найден на странице"

    def check_dropdown_filters(self, filters: list):
        """Проверка, что выпадающие фильтры присутствуют на странице"""

        for i in filters:
            assert i in self.drop_filters.filter_dict, f"фильтр {i} не найден на странице"

    def check_load_page(self):
        self.advertising.check_visible(12)
        self.filters.check_load_filters()
        self.check_button_filters(["Фильмы", "Сериалы", "С высоким рейтингом", "Российские", "Зарубежные", "Вышедшие",
                            "Скрыть просмотренные", "Загрузить на смартфоне"])
        self.drop_filters.check_load_filters()
        self.check_dropdown_filters(["Все страны", "Все жанры", "Все годы"])

    def get_films(self) -> list:
        """Получить список фильмов на странице"""

        lst = self.list_film.find_elements()
        for i, elem in enumerate(lst):
            lst[i] = elem.text

        return lst