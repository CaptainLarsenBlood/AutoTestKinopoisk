from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from elements.filter import ButtonFilterList


class TopFilms(BasePage):
    """PO для страниц с топ фильмами"""

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.filters = ButtonFilterList(self.driver, By.CSS_SELECTOR, ".styles_root__omMgy")

    def check_filters(self, filters: list):
        """Проверка, что фильтры присутствуют на странице"""

        self.filters.get_filters()

        for i in filters:
            assert i in self.filters.filter_dict, f"фильтр {i} не найден на странице"

    def check_load_page(self):
        self.check_filters(["Фильмы", "Сериалы", "С высоким рейтингом", "Российские", "Зарубежные", "Вышедшие",
                                   "Скрыть просмотренные", "Загрузить на смартфоне"])

    '''def select_user(self, text: str):
        select = Select(self.browser.find_element(By.ID, 'userSelect'))
        select.select_by_visible_text(text)

    def check_load_page(self):
        customer = self.find_element(*TopFilmsLocators.FILTERS)
        customer.is_displayed()

    def select_login_type(self, custom: bool = True):
        if custom:
            self.browser.find_element(*LoginPageLocators.CUSTOMER_LOGIN).click()
        else:
            self.browser.find_element(*LoginPageLocators.MANAGER_LOGIN).click()

    def login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN).click()'''