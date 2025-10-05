from selenium import webdriver
from selenium.webdriver.common.by import By

max_screen = webdriver.ChromeOptions()
max_screen.add_argument("--start-maximized")
driver = webdriver.Chrome(max_screen)
driver.get("https://www.w3schools.com/sql/sql_alter.asp")
driver.implicitly_wait(10)

table_header_list = driver.find_elements(By.XPATH, "(//table[@class='ws-table-all notranslate'])[2]")

for list in table_header_list:
    print(list.text)

print("\t")
print("\nTable header is printed")

driver.quit()