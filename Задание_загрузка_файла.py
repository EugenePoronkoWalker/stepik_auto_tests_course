from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Open a browser
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill in all fields
    firstname = browser.find_element(By.CSS_SELECTOR, 'input[name = "firstname"]')
    firstname.send_keys("Eugene")

    lastname = browser.find_element(By.CSS_SELECTOR, 'input[name = "lastname"]')
    lastname.send_keys("Poronko")

    email_address = browser.find_element(By.CSS_SELECTOR, 'input[name = "email"]')
    email_address.send_keys("eugene@test.com")

    # Download a test file
    button = browser.find_element(By.CSS_SELECTOR, 'input[name = "file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'seleniumtest.txt')
    button.send_keys(file_path)

    # Click on the "Submit" button
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

finally:
    # Wait for checking results on a page
    time.sleep(10)
    # Close your browser after manipulation
    browser.quit()
