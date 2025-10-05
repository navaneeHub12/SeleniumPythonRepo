import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(5)

#Loggin part with username: standard_user and Pwd: secret_sauce
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")

#Click Submit button:
driver.find_element(By.ID, "login-button").click()

#Once logged in..
#Capture the displayed list of items title. This page contain lot of items, so we need to use elements
titles = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")

#Use for each loops to print item titles
print("List of Items in the Sauce Demo web site")
for title in titles:
    print(title.text)

time.sleep(5)
driver.quit()




