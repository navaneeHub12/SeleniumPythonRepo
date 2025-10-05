from selenium import webdriver
from selenium.webdriver.common.by import By

max_page = webdriver.ChromeOptions()
max_page.add_argument("--start-maximized")
driver = webdriver.Chrome(max_page)

driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/html/html_tables.asp")

companies_list = driver.find_elements(By.XPATH, "//table[@class='ws-table-all']//td[1]")

for company in companies_list:
    print(company.text, end=" ")
    print(" ")
    
print("Company names are printed")
driver.quit()

