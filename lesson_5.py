import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/registration1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_field = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    first_name_field.send_keys('Ilias')

    last_name_field = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    last_name_field.send_keys('Badretdinov')

    mail_field = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    mail_field.send_keys('hello@mail.ru')

    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()


