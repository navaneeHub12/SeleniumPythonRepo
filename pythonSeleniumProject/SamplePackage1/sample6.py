import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)

driver.get("https://www.google.com/")

driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("Selenium Python")
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)

time.sleep(5)

search_result = driver.find_elements(By.XPATH,"//h3[@class='LC20lb MBeuO DKV0Md']")


for title_list in search_result:
    for i in range(6):
        title_name = title_list.text

time.sleep(5)
driver.quit()

