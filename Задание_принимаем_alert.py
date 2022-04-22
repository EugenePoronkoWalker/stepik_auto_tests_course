from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    # Open a browser
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Find a button and click on it
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Confirm alert
    confirm = browser.switch_to.alert
    confirm.accept()

    # Solve an exercise on a new page
    x_element = browser.find_element(By.ID,"input_value")
    x = int(x_element.text)
    result = calc(x)
    # Write an answer
    field = browser.find_element(By.ID, "answer")
    field.send_keys(result)
    # Click on the"Submit" button
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

