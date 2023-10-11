from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

parent_page_text_header="An iFrame containing the TinyMCE WYSIWYG Editor"

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("http://the-internet.herokuapp.com/iframe")
print(f"1st window title:`{driver.title}`.")

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("New text in iframes")
driver.save_screenshot("screenshots/python-iframes-1.png")

driver.switch_to.default_content()
actual_page_header_text = driver.find_element(By.CSS_SELECTOR, 'h3').text
print(f"actual_page_header_text: {actual_page_header_text}")

driver.close()
assert actual_page_header_text == parent_page_text_header