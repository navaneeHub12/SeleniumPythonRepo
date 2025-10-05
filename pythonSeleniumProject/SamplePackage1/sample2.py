import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(5)

check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for check_box in check_boxes:
    if check_box.is_selected():
        check_box.click()
        print(check_box.text,"is checked")
    else:
        check_box.click()
        print(check_box.text, "is checked")
time.sleep(5)
driver.quit()