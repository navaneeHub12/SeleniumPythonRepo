import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_full = webdriver.ChromeOptions()
chrome_full.add_argument("--kiosk")
driver = webdriver.Chrome(chrome_full)

driver.get("https://omayo.blogspot.com/")

print(driver.title)

time.sleep(5)
driver.quit()
