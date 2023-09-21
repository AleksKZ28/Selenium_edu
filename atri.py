from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(url)
treasure = browser.find_element(By.ID, "treasure")
x = treasure.get_attribute("valuex")
y = calc(x)
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

input2 = browser.find_element(By.ID, 'robotCheckbox')
input2.click()

input3 = browser.find_element(By.ID, 'robotsRule')
input3.click()

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(30)
browser.quit()





