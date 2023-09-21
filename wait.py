import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def cacl(x):
    return str(math.log(abs(12 * math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button1 = browser.find_element(By.ID, "book")
button1.click()

x_element = browser.find_element(By.ID, "input_value")
x = int(x_element.text)
y = cacl(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button2 = browser.find_element(By.ID, "solve")
button2.click()

time.sleep(30)
browser.quit()



