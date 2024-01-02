import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_service=Service("C:\\Users\\DELL\\Downloads\\chromedriver-win64")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/frames")
iframe = driver.find_element(By.CSS_SELECTOR, "google-efs") 
driver.switch_to.frame(iframe)
element_inside_iframe = driver.find_element(By.XPATH, "//input[@id='element_inside_iframe_id']")
element_inside_iframe.send_keys("This is iframe")
driver.switch_to.default_content()
driver.quit()
