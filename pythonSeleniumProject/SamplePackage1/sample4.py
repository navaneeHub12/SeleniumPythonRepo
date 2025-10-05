import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)

#---------Simple Alert---------------
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()

simple_alert = driver.switch_to.alert
print("Simple alert text info: ", simple_alert.text)
simple_alert.accept()
time.sleep(7)
#---------Confirm Alert---------------
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()

confirm_alert = driver.switch_to.alert
print("Confirm alert text info: ", confirm_alert.text)
confirm_alert.accept()
time.sleep(7)


#---------Confirm Alert---------------
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

prompt_alerts = driver.switch_to.alert
print("Prompt alert text info: ", prompt_alerts.text)
prompt_alerts.send_keys("Navaneethakrishnan")
prompt_alerts.accept()
time.sleep(7)

driver.quit()

