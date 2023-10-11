import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

promo_code_invalid = "SOME_PROMO-CODE"
promo_code_valid = "rahulshettyacademy"

search_pattern = "ber"

expected_list =["Cucumber", "Raspberry", "Strawberry"]


service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(2)

wait = WebDriverWait(driver, 10)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys(search_pattern)
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,".search-button").click()

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# test exercise: about web-element list - begin
exercise_list = driver.find_elements(By.CSS_SELECTOR,"div h4.product-name")
for text_element in exercise_list:
    print(f"here is product name", text_element.text)
    assert search_pattern in text_element.text

    checkif = any(item in text_element.text for item in expected_list)
    print(checkif)
    assert checkif
# test exercise: about web-element list - done

for search in results:
    # print(f"found element with text:`{search.text}`.")
    search.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a.cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# test validation
page_sum = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
price_from_cell = 0
for price in prices:
    price_from_cell = price_from_cell + int(price.text)

print(f"From table cell:`{price_from_cell}`")
print(f"From Summary cell :`{page_sum}`")

assert price_from_cell == page_sum

driver.find_element(By.CLASS_NAME, "promoCode").send_keys(promo_code_valid)

driver.find_element(By.CLASS_NAME, "promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

# test exercise: about summary - begin

discount_percent = int(driver.find_element(By.CSS_SELECTOR, ".discountPerc").text[:-1])
page_sum_discounted = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print("float price with discount ",page_sum_discounted)

print(f"Total amount:`{page_sum}`")
print(f"Total amount:`{discount_percent}`")
print(f"Total amount with discount:`{page_sum_discounted}`")

result_sum = page_sum*(1-discount_percent/100)

print(f"process summary:`{result_sum}`")

assert page_sum_discounted < page_sum
assert page_sum_discounted == page_sum_discounted

# test exercise: about summary - done

print(f"last test step text: `{driver.find_element(By.CLASS_NAME, 'promoInfo').text}`.")

driver.save_screenshot("screenshots/python-waits-1.png")

driver.close()
