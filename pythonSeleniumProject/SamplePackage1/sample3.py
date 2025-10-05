import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(5)

dropdown_list = driver.find_element(By.ID,'dropdown')
selects = Select(dropdown_list)
selects.select_by_value("2")

time.sleep(4)
print("Option 2 is successfully selected")
driver.quit()