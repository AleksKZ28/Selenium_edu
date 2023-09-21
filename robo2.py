from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(url)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

input2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
input2.click()

input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
input3.click()

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(30)
browser.quit()

print(x)