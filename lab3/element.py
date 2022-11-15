from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locator import RegistrationPageLocator

from locator import MainPageLocator


class BasePageElement:
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*self.locator)
        )
        # driver.find_element_my_name(self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element(*self.locator)
        )
        element = driver.find_element(*self.locator)
        return element.get_attribute('value')


class SearchProductElement(BasePageElement):
    locator = MainPageLocator.SEARCH_FIELD


class FirstNameElement(BasePageElement):
    locator = RegistrationPageLocator.FIRST_NAME_FIELD


class LastNameElement(BasePageElement):
    locator = RegistrationPageLocator.LAST_NAME_FIELD


class EmailElement(BasePageElement):
    locator = RegistrationPageLocator.EMAIL_FIELD


class PasswordElement(BasePageElement):
    locator = RegistrationPageLocator.PASSWORD_FIELD


class ConfirmPasswordElement(BasePageElement):
    locator = RegistrationPageLocator.CONFIRM_PASSWORD_FIELD


