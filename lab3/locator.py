from selenium.webdriver.common.by import By


class MainPageLocator:
    ACCOUNT_BUTTON = (By.XPATH, "//a[@class='skip-link skip-account']")
    REGISTER_BUTTON = (By.XPATH, "//a[@title='Register']")

    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")


class RegistrationPageLocator:
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@name='lastname']")
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@title='Password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@id='confirmation']")
    IS_SUBSCRIBED_CHECKBOX = (By.XPATH, "//input[@id='is_subscribed']")
    REGISTER_BUTTON = (By.XPATH, "//button[@title='Register']")


class SearchPageLocator:
    VIEW_DETAILS_BUTTON = (By.XPATH, "//a[@title='View Details']")


class ProductDetailLocator:
    DETAIL_CHECKBOX = (By.ID, "links_20")
    ADD_TO_WISHLIST_BUTTON = (By.XPATH, "//a[@class='link-wishlist']")

