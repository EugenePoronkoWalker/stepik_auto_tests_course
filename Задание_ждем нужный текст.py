from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    # Open a browser
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element(By.ID, "book").click()

    # Solve an exercise on a new page
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = calc(x)
    # Write an answer
    field = browser.find_element(By.ID, "answer")
    field.send_keys(result)
    # Click on the"Submit" button
    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()