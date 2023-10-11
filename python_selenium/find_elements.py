import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from selenium.webdriver.common.by import By

service_obj = Service()  # selenium_manager
driver = webdriver.Chrome(service = service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print('driver.title: ',driver.title)
print(f"current url: {driver.current_url}")


# Auto-suggestive dynamic dropdown
driver.find_element(By.ID,"autosuggest").send_keys("ind")

time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    print(f"country: {country.text}")

    if country.text == "India":
        country.click()
        break
print(f" by element text:`{driver.find_element(By.ID,'autosuggest').text}`.")
print(f" by element attribute value:`{driver.find_element(By.ID,'autosuggest').get_attribute('value')}`.")


assert driver.find_element(By.ID,'autosuggest').get_attribute('value') == "India"
