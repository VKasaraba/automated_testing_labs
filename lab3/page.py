from element import BasePageElement
from element import SearchProductElement
from element import ConfirmPasswordElement, EmailElement, FirstNameElement, LastNameElement, PasswordElement
from locator import ProductDetailLocator
from locator import SearchPageLocator
from locator import RegistrationPageLocator
from locator import MainPageLocator


class BasePage:
    def __init__(self, driver) -> None:
        self.driver = driver


class MainPage(BasePage):
    search_product_element = SearchProductElement()

    def click_account_button(self):
        element = self.driver.find_element(*MainPageLocator.ACCOUNT_BUTTON)
        element.click()

    def click_register_button(self):
        element = self.driver.find_element(*MainPageLocator.REGISTER_BUTTON)
        element.click()

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocator.SEARCH_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    def click_view_details_button(self):
        element = self.driver.find_element(*SearchPageLocator.VIEW_DETAILS_BUTTON)
        element.click()

    def is_results_found(self):
        searched_product = MainPage(self.driver).search_product_element
        if 'Your search returns no results.' in self.driver.page_source:
            return False
        elif searched_product in self.driver.page_source:
            return True
        return False


class RegistrationPage(BasePage):
    first_name_element = FirstNameElement()
    last_name_element = LastNameElement()
    email_element = EmailElement()
    password_element = PasswordElement()
    confirm_password_element = ConfirmPasswordElement()

    def click_is_subscribed_checkbox(self):
        element = self.driver.find_element(*RegistrationPageLocator.IS_SUBSCRIBED_CHECKBOX)
        element.click()

    def click_register_button(self):
        element = self.driver.find_element(*RegistrationPageLocator.REGISTER_BUTTON)
        element.click()

    def is_registration_successful(self):
        return 'Thank you for registering with Madison Island.' in self.driver.page_source


class ProductDetailPage(BasePage):
    def click_detail_checkbox(self):
        element = self.driver.find_element(*ProductDetailLocator.DETAIL_CHECKBOX)
        element.click()

    def click_add_to_wishlist_button(self):
        element = self.driver.find_element(*ProductDetailLocator.ADD_TO_WISHLIST_BUTTON)
        element.click()

    def is_added_to_wishlist(self):
        print(self.driver.page_source)
        return 'has been added to your wishlist' in self.driver.page_source or 'Welcome' in self.driver.page_source