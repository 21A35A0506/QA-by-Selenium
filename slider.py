import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_service=Service("C:\\Users\\DELL\\Downloads\\chromedriver-win64")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/slider") 
slider=getattr((By.XPATH,"//input[@type='range]"))
desired_value = 50 
actions=getattr(driver)
slider_width = slider.size['width']
actions.click_and_hold(slider).move_by_offset(slider_width * desired_value / 100, 0).release().perform()
driver.quit()
