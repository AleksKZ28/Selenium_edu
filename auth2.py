from selenium.webdriver.common.by import By
import time



try:
    input1=browser.find_element(By.CSS_SELECTOR ,"[placeholder~='first']")
    input1.send_keys('Sasha')
    input2=browser.find_element(By.CSS_SELECTOR, "[placeholder~='last']")
    input2.send_keys('Kuznetsov')
    input3=browser.find_element(By.CSS_SELECTOR, "[placeholder~='email']")
    input3.send_keys('aleks@mail.ru')


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)


    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)

    browser.quit()