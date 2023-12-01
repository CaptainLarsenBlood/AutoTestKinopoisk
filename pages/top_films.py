from pages.base_page import BasePage
from elements.basic_elements import Element
from selenium.webdriver.common.by import By
from elements.filter import ButtonFilterList, DropDownFilterList


class TopFilms(BasePage):
    """PO для страниц с топ фильмами"""

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.filters = ButtonFilterList(self.driver, By.CSS_SELECTOR, ".styles_root__omMgy")
        self.drop_filters = DropDownFilterList(self.driver, By.CSS_SELECTOR, '.styles_selectButton__4xHt7')
        self.advertising = Element(self.driver, By.CSS_SELECTOR, '.styles_container__XXCpX ')
        self.list_film = Element(self.driver, By.CSS_SELECTOR, ".styles_mainTitle__IFQyZ")

    def check_filters(self, filters: list):
        """Проверка, что фильтры присутствуют на странице"""

        for i in filters:
            assert i in self.filters.filter_dict, f"фильтр {i} не найден на странице"

    def check_load_page(self):
        self.advertising.check_visible(12)
        self.filters.check_load_filters()
        self.check_filters(["Фильмы", "Сериалы", "С высоким рейтингом", "Российские", "Зарубежные", "Вышедшие",
                            "Скрыть просмотренные", "Загрузить на смартфоне"])

    def get_films(self) -> list:
        """Получить список фильмов на странице"""

        lst = self.list_film.find_elements()
        for i, elem in enumerate(lst):
            lst[i] = elem.text

        return lst
    '''def check_load_page(self):
        customer = self.find_element(*TopFilmsLocators.FILTERS)
        customer.is_displayed()

    def select_login_type(self, custom: bool = True):
        if custom:
            self.browser.find_element(*LoginPageLocators.CUSTOMER_LOGIN).click()
        else:
            self.browser.find_element(*LoginPageLocators.MANAGER_LOGIN).click()

    def login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN).click()'''