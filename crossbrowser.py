from selenium import webdriver
import time

browsers = ["chrome", "firefox", "edge"]

for browser in browsers:
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print(f"{browser} is not supported.")
        continue

    driver.get("https://www.google.com")
    print(f"Opened Google in {browser}")
    time.sleep(3)
    driver.quit()

for browser in ["chrome", "firefox", "edge"]:
    test_cross_browser(browser)
