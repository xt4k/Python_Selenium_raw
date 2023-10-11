from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

unsorted_list =[]
sorted_list =[]

def get_vegetable_list(driver):
    return driver.find_elements(By.XPATH,"//tr/td[1]")

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(2)
# driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.ID,"page-menu").click()
driver.find_element(By.ID,"page-menu").send_keys("2")
driver.find_element(By.ID,"page-menu").click()

unsorted = get_vegetable_list(driver)

for item in unsorted:
    unsorted_list.append(item.text)
print(f"unsorted list:`{unsorted_list}`.")

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

sorted = get_vegetable_list(driver)

for item in sorted:
    sorted_list.append(item.text)
driver.close()

unsorted_list.sort()

print(f"actual sorted list:`{sorted_list}`.")
print(f"sorting unsorted list:`{unsorted_list}`.")

assert sorted_list == unsorted_list
