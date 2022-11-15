import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


DRIVER_PATH = '/Users/macbookpro131/projects/personal/NULP/testing/chromedriver'
WEBSITE_PATH = 'http://suninjuly.github.io/explicit_wait2.html'
# Init the driver
driver = webdriver.Chrome(DRIVER_PATH)

# Open web page
driver.get(WEBSITE_PATH)

# Wait until the price is $100
WebDriverWait(driver, timeout=30).until(lambda d: d.find_element(By.ID, "price").text == '$100')

# Press the 'Book' button
book_button_element = driver.find_element(By.ID, "book")
book_button_element.click()

# Solve the math problem
x_element = driver.find_element(By.ID, "input_value")
x_value = float(x_element.text)
result = log(abs(12*sin(x_value)))

input_bar_element = driver.find_element(By.ID, "answer")
input_bar_element.send_keys(result)

submit_button_element = driver.find_element(By.ID, "solve")
submit_button_element.click()

time.sleep(100)
driver.quit()