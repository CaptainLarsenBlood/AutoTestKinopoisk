import pytest
from selenium import webdriver


class DriverManager(object):

    def __init__(self):
        self._instance = None

    def start(self):
        if self._instance is None:
            self._instance = webdriver.Chrome()
        return self._instance

    def stop(self):
        self._instance.quit()


@pytest.fixture(scope="class")
def driver(request):
    print("\nstart browser for test..")
    driver = DriverManager()
    request.cls.driver = driver.start()
    yield driver
    driver.stop()
    print("\nstop browser")
