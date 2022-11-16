from selenium import webdriver
from unittest import TestCase, main
from page import ProductDetailPage
from page import RegistrationPage
from page import MainPage, SearchResultsPage
from faker import Faker


DRIVER_PATH = '/Users/macbookpro131/projects/personal/NULP/testing/chromedriver'
WEBSITE_PATH = 'http://demo-store.seleniumacademy.com'

class GoodsSearch(TestCase):
    def setUp(self):
        # Before each test: init the driver and opend a web page
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.driver.get(WEBSITE_PATH)
        self.fake = Faker()

    def test_search_products_with_invalid_input(self):
        ''' Test that we see "No results found" if search for something non-existent '''
        main_page = MainPage(self.driver)
        main_page.search_product_element = 'lkndsaglkjdlsajgnpodas'
        main_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)
        assert not search_results_page.is_results_found()

    def test_search_products_with_valid_input(self):
        ''' Test that we see the product we searched for on the Search Result page '''
        main_page = MainPage(self.driver)
        main_page.search_product_element = 'LAFAYETTE CONVERTIBLE DRESS'
        main_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)
        assert search_results_page.is_results_found()

    def test_new_user_registration(self):
        ''' Test that new user is created '''
        main_page = MainPage(self.driver)
        main_page.click_account_button()
        main_page.click_register_button()
        registration_page = RegistrationPage(self.driver)
        registration_page.first_name_element = self.fake.name().split(' ')[0]
        registration_page.last_name_element = self.fake.name().split(' ')[1]
        registration_page.email_element = self.fake.email()
        password = self.fake.password()
        registration_page.password_element = password
        registration_page.confirm_password_element = password
        registration_page.click_is_subscribed_checkbox()
        registration_page.click_register_button()
        assert registration_page.is_registration_successful()

    def test_add_to_wishlist(self):
        ''' Test that selected product is added to wishlist '''
        main_page = MainPage(self.driver)
        main_page.search_product_element = 'interesting book'
        main_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)
        search_results_page.click_view_details_button()
        detail_page = ProductDetailPage(self.driver)
        detail_page.click_detail_checkbox()
        detail_page.click_add_to_wishlist_button()
        assert detail_page.is_added_to_wishlist()


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    main()