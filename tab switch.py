from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
print("Opened Tab 1: Google")
time.sleep(2)

driver.execute_script("window.open('https://www.bing.com', '_blank');")
print("Opened Tab 2: Bing")
time.sleep(2)

tabs = driver.window_handles

driver.switch_to.window(tabs[1])
print("Switched to Tab 2")
time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()
print("Searched in Tab 2")
time.sleep(3)

driver.switch_to.window(tabs[0])
print("Switched back to Tab 1")
time.sleep(2)

# Close all tabs
driver.quit()
