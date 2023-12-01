
class BasePage:
    """Базовый класс для страниц"""

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def go_to_site(self):
        return self.driver.get(self.base_url)
