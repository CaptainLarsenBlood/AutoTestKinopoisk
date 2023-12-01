from typing import List

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class Element:
    """Базовый класс для всех элементов"""

    def __init__(self, driver, strategy, locator):

        self.driver = driver
        self.locator = (strategy, locator)

    def find_element(self, time=10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.locator),
                                                      message=f"Не найден элемент {self.locator}")

    def check_visible(self, time=10) -> WebElement:

        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(self.locator),
                                                      message=f"Элемент не виден на странице{self.locator}")

    def find_elements(self, time=10) -> list[WebElement]:
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(self.locator),
                                                      message=f"Не найдены элементы {self.locator}")