import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

time.sleep(5)

parent_window_id = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Open a popup window").click()

child_windows = driver.window_handles

for window in child_windows:
    driver.switch_to.window(window)
    if driver.title.__eq__("New Window"):
        print(driver.find_element(By.CLASS_NAME,"example").text)
        break

driver.switch_to.window(parent_window_id)
time.sleep(5)
driver.find_element(By.ID, "ta1").send_keys("This is Python programming")

print("Test execution completed")

