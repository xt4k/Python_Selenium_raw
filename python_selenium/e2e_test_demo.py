from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

expected_product_name = "Blackberry"

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(2)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
driver.save_screenshot("screenshots/python-e2e-1.png")

shop_list = driver.find_elements(By.XPATH, "//app-card/div")
print(f"shop_list:`{shop_list}`.")

for element in shop_list:
    actual_element_text = element.find_element(By.TAG_NAME, 'h4').text
    image_name = element.find_element(By.TAG_NAME, "img").get_attribute("src")

    print(f"element text:`{actual_element_text}`, image_name:`{image_name}`.")
    driver.save_screenshot(f"screenshots/python-e2e-2-{image_name}.png")

    if actual_element_text == expected_product_name:
        assert expected_product_name.lower() in image_name.lower()

driver.save_screenshot("screenshots/python-e2e-3.png")

driver.close()
