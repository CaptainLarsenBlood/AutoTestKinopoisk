from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class MoneyPage(BasePage):

    '''def select_operation(self, type_oper: str = 'trans'):
        wait = WebDriverWait(self.browser, timeout=3)

        match type_oper:
            case 'trans':
                self.browser.refresh()
                self.browser.find_element(*MoneyPageLocators.TRANSACTIONS).click()
                wait.until(lambda x: self.browser.find_element(By.CSS_SELECTOR, ".table").is_displayed())

            case 'deposit':
                self.browser.find_element(*MoneyPageLocators.DEPOSIT).click()
                wait.until(lambda x: self.browser.find_element(*MoneyPageLocators.SUBMIT).text == "Deposit")

            case 'with':
                self.browser.find_element(*MoneyPageLocators.WITHDRAWL).click()
                wait.until(lambda x: self.browser.find_element(*MoneyPageLocators.SUBMIT).text == "Withdraw")

    def input_money_and_submit(self, amount: [str, int] = None):

        self.browser.find_element(*MoneyPageLocators.AMOUNT_INP).send_keys(amount)
        self.browser.find_element(*MoneyPageLocators.SUBMIT).click()

    def check_balance(self, balance: int = 0):

        assert balance == int(self.browser.find_element(*MoneyPageLocators.INFO_ACCOUNT).text), \
            f"Баланс должен быть {balance}!"

    def get_line_transaction(self, line: [str, int]) -> str:
        return self.browser.find_element(By.CSS_SELECTOR, f'[id=anchor{line}').text'''
