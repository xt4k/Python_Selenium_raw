from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from selenium.webdriver.common.by import By

service_obj = Service()  # selenium_manager
driver = webdriver.Chrome(service = service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")


for checkbox in checkboxes:
    print(f"checkbox name: {checkbox.get_attribute('name')}")
    if checkbox.get_attribute("value") == "option3":
        if not checkbox.is_selected():
            checkbox.click()
        assert(checkbox.is_selected())
        break


radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")

for radiobutton in radiobuttons:
    print(f"radiobutton value: {radiobutton.get_attribute('value')}")

    if radiobutton.get_attribute("value") == "radio3" or radiobutton.get_attribute("value") == "radio2":
        if not radiobutton.is_selected():
            radiobutton.click()
            driver.save_screenshot(f"screenshots/python-ui-controls-1-{radiobutton.get_attribute('value')}.png")
        assert (radiobutton.is_selected())
driver.save_screenshot("screenshots/python-ui-controls-3.png")

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID,"hide-textbox").click()

assert not driver.find_element(By.ID, "displayed-text").is_displayed()

driver.close()
