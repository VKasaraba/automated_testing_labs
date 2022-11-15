from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By


DRIVER_PATH = '/Users/macbookpro131/projects/personal/NULP/testing/chromedriver'
WEBSITE_PATH = 'http://suninjuly.github.io/math.html'

# Init the driver
driver = webdriver.Chrome(DRIVER_PATH)

# Open web page
driver.get(WEBSITE_PATH)

# Get value for 'x' and calculate the result of the math problem
x_element = driver.find_element(By.ID, "input_value")
x_value = float(x_element.text)
result = log(abs(12*sin(x_value)))

# Put in the calculated result
input_bar_element = driver.find_element(By.ID, "answer")
input_bar_element.send_keys(result)

# Click the "I'm the robot" checkbox
checkbox_element = driver.find_element(By.ID, "robotCheckbox")
checkbox_element.click()

# Select the 'Robots rule' option
selection_element = driver.find_element(By.ID, "robotsRule")
selection_element.click()

# Press the 'Submit' button
submit_button_element = driver.find_element(By.TAG_NAME, "button")
submit_button_element.click()

driver.quit()
