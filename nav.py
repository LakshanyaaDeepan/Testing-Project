from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

drv = webdriver.Chrome()

drv.get("https://www.google.com")
print("Opened Google")
time.sleep(2)

box = drv.find_element(By.NAME, "q")
box.send_keys("GeeksforGeeks", Keys.RETURN)
print("Searched for GeeksforGeeks")
time.sleep(3)

drv.back()
print("⬅ Navigated back to Google")
time.sleep(3)

drv.forward()
print("Navigated forward to search results")
time.sleep(4)




drv.quit()
print("Closed browser")
