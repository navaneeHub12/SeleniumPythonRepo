import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(5)

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

logged_in_info = driver.find_element(By.CLASS_NAME, "post-title").text
logged_in_text = "Logged In Successfully"
if logged_in_info == logged_in_text:
    print("Logged In Successfully is displayed")
else:
    print("Logged In Successfully is not displayed")

time.sleep(5)

driver.quit()
