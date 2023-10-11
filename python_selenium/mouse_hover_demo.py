from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
driver.save_screenshot("screenshots/python-mouse-hover-1.png")

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

driver.save_screenshot("screenshots/python-mouse-hover-2.png")

assert (not driver.find_element(By.LINK_TEXT, "Reload").is_displayed())