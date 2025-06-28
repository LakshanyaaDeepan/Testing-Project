from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Firefox()
browser.get('https://demoqa.com/checkbox')
browser.maximize_window()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element(By.XPATH, "//span[@class='rct-title' and text()='Home']").click()
time.sleep(3)
browser.quit()