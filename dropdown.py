from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

account_list = driver.find_element(By.ID, "nav-link-accountList")

actions = ActionChains(driver)
actions.move_to_element(account_list).perform()

time.sleep(3)

driver.find_element(By.LINK_TEXT, "Your Orders").click()


time.sleep(3)
driver.quit()


