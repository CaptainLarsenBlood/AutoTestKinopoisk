from elements.basic_elements import Element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FilterList(Element):
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

    def check_load_filters(self):
        self.get_filters()
        assert len(self.filter_dict) != 0, "Фильтры не загрузились"


class ButtonFilterList(FilterList):
    """Список кнопочных фильтров"""

    filter_dict = {}

    def __init__(self, driver, strategy, locator):
        super().__init__(driver, strategy, locator)

    def select_filter(self, text: str):
        """Выбор фильтра
        :param text - название кнопочного фильтра"""

        self.check_load_filters()
        self.filter_dict[text].click()
        assert "styles_active" in self.filter_dict[text].get_attribute("class"), f"Фильтр {text} не выбрался"


class DropDownFilterList(FilterList):
    """Список выпадающих фильтров"""

    filter_dict = {}

    def __init__(self, driver, strategy, locator):
        super().__init__(driver, strategy, locator)

    def select_filter(self, filter_name: str, item_menu: str):
        """Выбрать значение из выпадающего фильтра
        :param filter_name - тип фильтра (Страны, Жанры, Годы)
        :param item_menu - подтип фильтра"""

        self.check_load_filters()
        self.filter_dict[filter_name].click()

        item_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".styles_item__swkWa")),
                                               message=f"Не найдены элементы списка")

        for el in item_list:
            if el.text == item_menu:
                el.click()
                break
        assert self.filter_dict[filter_name].text == item_menu, f"Фильтр {item_menu} не выбрался"




