import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/simple_form_find_task.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_field = browser.find_element(By.CSS_SELECTOR, "[name='first_name']")
    first_name_field.send_keys('Ilias')

    last_name_field = browser.find_element(By.CSS_SELECTOR, "[name='last_name']")
    last_name_field.send_keys('Badretdinov')

    city_field = browser.find_element(By.CLASS_NAME, "form-control.city")
    city_field.send_keys('Kazan')

    country_field = browser.find_element(By.ID, "country")
    country_field.send_keys('Russia')

    submit_button = browser.find_element(By.ID, "submit_button")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
