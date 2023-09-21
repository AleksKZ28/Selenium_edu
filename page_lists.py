from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.remote.webelement import WebElement


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
num1 = browser.find_element(By.ID, "num1")
numb1 = int(num1.text)
num2 = browser.find_element(By.ID, "num2")
numb2 = int(num2.text)
x = str(numb1 + numb2)
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(x)
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(30)
browser.quit()