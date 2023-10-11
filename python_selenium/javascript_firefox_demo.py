from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By


initial_page_title = "Practice Page"


options = webdriver.FirefoxOptions()
options.add_argument("-headless")
# options.add_argument('--log info')
# options.log.level='info'
#options.log= 'logs/gecko_log.log'
# options.headless = True

# service_obj1= Service()
service_obj = webdriver.FirefoxService(log_output='logs/gecko.log', service_args=['--log', 'debug'])
driver = webdriver.Firefox(service=service_obj, options=options)
driver.implicitly_wait(2)
# driver.maximize_window()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(f"1st window title:`{driver.title}`.")
driver.save_screenshot("screenshots/python-js-1.png")
assert driver.title == initial_page_title
#assert driver.find_element(By.ID,"gf-BIG").is_displayed()


driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.save_screenshot("screenshots/python-js-2.png")

assert driver.find_element(By.ID,"gf-BIG").is_displayed()
driver.close()
