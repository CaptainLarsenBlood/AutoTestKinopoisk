from selenium import webdriver
import pytest


@pytest.mark.usefixtures('driver')
class BaseTest(object):
    pass