import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID,"username").send_keys("student")
time.sleep(3)
driver.find_element(By.ID, "password").send_keys("Password123")

driver.find_element(By.XPATH,"//button[@id='submit']").click()

time.sleep(5)

logged_in_title = driver.find_element((By.XPATH,"//h1[@class='post-title']")).text
logged_in_display = driver.find_element((By.XPATH,"//h1[@class='post-title']")).is_displayed()

print("After logged in", logged_in_title)
print("Logged in Successfully message is displayed", logged_in_display)

time.sleep(5)

driver.quit()

