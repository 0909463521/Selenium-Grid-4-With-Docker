from selenium import webdriver
import time
# Connect to the remote WebDriver server
options = webdriver.ChromeOptions()
options.set_capability("browserVersion","124.0")
# options.set_capability("platformName","linux")


driver = webdriver.Remote(command_executor="http://127.0.0.1:4444", options=options)


driver.get("https://www.google.com/")
title = driver.title
print(title)
time.sleep(10)
driver.quit()