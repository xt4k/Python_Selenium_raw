from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
web_page_header =driver.find_element(By.CSS_SELECTOR, "h3").text
print(f"Main window: `{web_page_header}`.")

driver.find_element(By.XPATH, "//h3//following-sibling::*[1]").click()
driver.save_screenshot("screenshots/python-child-window-1.png")

opened_windows = driver.window_handles# print(f"opened windows: `{opened_windows}`.")
driver.switch_to.window(opened_windows[1])# print(driver.find_element(By.TAG_NAME,"h3").text)

child_text = driver.find_element(By.TAG_NAME,"h3").text
print(f"child windows: `{child_text}`.")
driver.save_screenshot("screenshots/python-child-window-2.png")
driver.close()

driver.switch_to.window(opened_windows[0])
print(f"Again main  window: `{driver.find_element(By.CSS_SELECTOR,'h3').text}`.")
driver.save_screenshot("screenshots/python-child-window-3.png")
driver.close()
