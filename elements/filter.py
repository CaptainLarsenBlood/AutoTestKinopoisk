from elements.basic_elements import Element



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