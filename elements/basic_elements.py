from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Element:
    """Базовый класс для всех элементов"""

    def __init__(self, driver, strategy, locator):

        self.driver = driver
        self.locator = (strategy, locator)

    def find_element(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.locator),
                                                      message=f"Не найден элемент {self.locator}")

    def check_visible(self, time=10):

        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(self.locator),
                                                      message=f"Элемент не виден на странице{self.locator}")

    def find_elements(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(self.locator),
                                                      message=f"Не найдены элементы {self.locator}")


class ButtonFilter(Element):
    """Класс Кнопки-фильтра"""

    def __init__(self, driver, strategy, locator):
        super().__init__(driver, strategy, locator)

    def click(self):

        self.find_element().click()


class List(Element):
    """Базовый списочный класс"""

    def __init__(self, driver, strategy, locator):
        super().__init__(driver, strategy, locator)


class ButtonFilterList(Element):
    """Список фильтров"""

    filter_dict = {}

    def __init__(self, driver, strategy, locator):
        super().__init__(driver, strategy, locator)

    def get_filters(self):
        """Получить словарь - название фильтра: webElement"""

        lst_filter = self.find_elements()

        if len(lst_filter) == 0:
            raise Exception("Фильтры не найдены")
        for el in lst_filter:
            self.filter_dict[el.text] = el

        return self.filter_dict

    def check_filters(self, filters: list):
        """Проверка, что фильтры присутствуют на странице"""

        if len(self.filter_dict) == 0:
            self.get_filters()

        for i in filters:
            assert i in self.filter_dict, f"фильтр {i} не найден на странице"

    def select_filter(self, text):
        """Выбор фильтра"""

        self.filter_dict[text].click()
        assert "styles_active" in self.filter_dict[text].get_attribute("class"), f"Фильтр {text} не выбрался"







