from selenium import webdriver
from selenium.webdriver.common.by import By


DRIVER_PATH = '/Users/macbookpro131/projects/personal/NULP/testing/chromedriver'
WEBSITE_PATH = 'http://demo-store.seleniumacademy.com/customer/account/create/'

# Init the driver
driver = webdriver.Chrome(DRIVER_PATH)

# Open web page
driver.get(WEBSITE_PATH)

user_info = {
    'first_name': 'Volodymyr',
    'last_name': 'Kasaraba',
    'email_address': 'the.best.student1@lpnu.ua',
    'password': 'my_secret_pass',
}

# Fill in personal data
first_name_input_element = driver.find_element(By.XPATH, "//input[@name='firstname']")
first_name_input_element.send_keys(user_info.get('first_name'))

last_name_input_element = driver.find_element(By.XPATH, "//input[@id='lastname']")
last_name_input_element.send_keys(user_info.get('last_name'))

email_address_input_element = driver.find_element(By.XPATH, "//input[@type='email']")
email_address_input_element.send_keys(user_info.get('email_address'))

password_input_element = driver.find_element(By.XPATH, "//input[@title='Password']")
password_input_element.send_keys(user_info.get('password'))

confirm_password_input_element = driver.find_element(By.XPATH, "//input[@id='confirmation']")
confirm_password_input_element.send_keys(user_info.get('password'))

# Click the "Sign Up for Newsletter" checkbox
subscribe_checkbox_element = driver.find_element(By.XPATH, "//input[@id='is_subscribed']")
subscribe_checkbox_element.click()

# Press the 'Register' button
register_button_element = driver.find_element(By.XPATH, "//button[@title='Register']")
register_button_element.click()

driver.quit()