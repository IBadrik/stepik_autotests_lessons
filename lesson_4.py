import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, 'input')
    for field in elements:
        field.send_keys('empty')

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
