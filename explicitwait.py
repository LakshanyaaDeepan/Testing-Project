from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))

search_box.send_keys("Selenium Python", Keys.RETURN)

wait.until(EC.visibility_of_element_located((By.ID, "search")))

print("Search results loaded!")

driver.quit()
