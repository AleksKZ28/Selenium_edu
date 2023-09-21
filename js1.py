import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = int(x_element.text)
y = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

ch = browser.find_element(By.ID, "robotCheckbox")
ch.click()

rb = browser.find_element(By.ID, "robotsRule")
rb.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(30)
browser.quit()



