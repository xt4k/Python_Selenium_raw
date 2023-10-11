from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

person_name = "some_new_person"

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys(person_name)

driver.save_screenshot("screenshots/python-alert-0.png")

driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert

print("alert text: ", alert.text)

assert person_name in alert.text

alert.accept()

driver.save_screenshot("screenshots/python-alert-1.png")

driver.close()
