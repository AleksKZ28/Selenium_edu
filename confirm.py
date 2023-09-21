from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def cacl(x):
    return str(math.log(abs(12 * math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.ID, 'input_value')
x = int(x_element.text)
y = cacl(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(30)
browser.quit()

