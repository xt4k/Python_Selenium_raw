from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

# web Chrome driver for Chrome browser

service_obj = Service()  # selenium_manager
driver = webdriver.Chrome(service = service_obj)
# driver = webdriver.Edge(service = service_obj)
## driver = webdriver.Firefox(service = service_obj)


driver.maximize_window()

driver.get("https://rahulshettyacademy.com")
print('driver.title: ',driver.title)
print(f"current url: {driver.current_url}")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME,"name").send_keys("Some Name")
driver.find_element(By.NAME,"email").send_keys("e-mail@gmail.com")

driver.find_element(By.ID,"exampleInputPassword1").send_keys("Password_1234")

driver.find_element(By.ID,"exampleCheck1").click()

driver.save_screenshot("screenshots/python-selenium-locators-1.png")

driver.find_element(By.NAME,"bday").send_keys("01/15/2000")

driver.save_screenshot("screenshots/python-selenium-locators-2.png")

#driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()

# Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.save_screenshot("screenshots/python-selenium-locators-3-1.png")

dropdown.select_by_visible_text("Male")

driver.save_screenshot("screenshots/python-selenium-locators-3-2.png")

dropdown.select_by_index(1)

driver.save_screenshot("screenshots/python-selenium-locators-3-3.png")

driver.find_element(By.XPATH,'//input[@value="Submit"]').click()# '//input[contains(@class,"btn-success")]').click()

success_message = driver.find_element(By.XPATH,'//div[contains(@class,"alert")]')
#success_message = driver.find_element(By.CLASS_NAME,"alert-success")

# driver.find_element(By.XPATH,"//strong")

message = success_message.text
print(f"final message: {message}")

assert "success" in message

driver.save_screenshot("screenshots/python-selenium-locators-2.png")

driver.close()