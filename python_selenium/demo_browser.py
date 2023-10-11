from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

# web Chrome driver for Chrome browser

service_obj = Service() # selenium_manager
driver = webdriver.Chrome(service = service_obj)
# driver = webdriver.Edge(service = service_obj)
## driver = webdriver.Firefox(service = service_obj)

# local chromedriver for Chrome browser
# service_obj = Service("C:\\Users\\Admin\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service = service_obj)

# local gecko-driver for Firefox browser
# service_obj = Service("C:\\Users\\Admin\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
# driver = webdriver.Firefox(service = service_obj)

# local edge-driver for Edge browser
# service_obj = Service("C:\\Users\\Admin\\Downloads\\edgedriver_win64\\msedgedriver.exe")
# driver = webdriver.Edge(service = service_obj)


driver.maximize_window()

driver.get("https://rahulshettyacademy.com")
print('driver.title: ',driver.title)
print(f"current url: {driver.current_url}")

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print('driver.title: ',driver.title)
print(f"current url: {driver.current_url}")
driver.save_screenshot("seleniumPractise-page.png")

driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()

driver.close()