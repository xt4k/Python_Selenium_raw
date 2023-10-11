from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_error_msg ="Incorrect username/password."

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

main_page_title = driver.title
print(f"1st window title:`{main_page_title}`.")

print(f"1st window link:`{driver.find_element(By.CLASS_NAME, 'blinkingText').text}`.")
driver.find_element(By.CLASS_NAME, "blinkingText").click()
driver.save_screenshot("screenshots/python-assignment-child-window-1.png")

opened_windows = driver.window_handles
driver.switch_to.window(opened_windows[1])

wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "strong a")))

print(f"2nd window:`{driver.title}`.")
email_address = driver.find_element(By.CSS_SELECTOR, "strong a").text
print(f"email_address: `{email_address}`.")
driver.save_screenshot("screenshots/python-assignment-child-window-2.png")
driver.close()

driver.switch_to.window(opened_windows[0])
print(f"Again 1st  window:`{driver.title}`.")
driver.save_screenshot("screenshots/python-assignment-child-window-3.png")

driver.find_element(By.ID,"username").send_keys(email_address)
driver.save_screenshot("screenshots/python-assignment-child-window-4.png")
driver.find_element(By.ID,"password").send_keys("password")
driver.save_screenshot("screenshots/python-assignment-child-window-5.png")

driver.find_element(By.ID,"signInBtn").click()
driver.save_screenshot("screenshots/python-assignment-child-window-6.png")

alert_locator = "div.alert"

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, alert_locator)))
driver.save_screenshot("screenshots/python-assignment-child-window-6.png")

err_msg =driver.find_element(By.CSS_SELECTOR, alert_locator).text

print(f"error text: {err_msg}")

assert err_msg == expected_error_msg

driver.close()
