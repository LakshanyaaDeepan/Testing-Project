from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.maximize_window()

input_box = driver.find_element(By.NAME, "firstname")


input_box.send_keys("Selenium Test")
time.sleep(1)

input_box.send_keys(Keys.CONTROL, 'z')
time.sleep(1)

input_box.send_keys(Keys.CONTROL, 'y')
time.sleep(1)

driver.quit()
