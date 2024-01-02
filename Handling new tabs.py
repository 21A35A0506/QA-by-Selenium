import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_service=Service("C:\\Users\\DELL\\Downloads\\chromedriver-win64")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/browser-windows")
parent=driver.current_window_handle 
link = driver.find_element(By.LINK_TEXT, "Click here to get new tab")  
child=driver.window_handles[1]
driver.switch_to.window(child)
time.sleep(3)
print(driver.title)
driver.close()
driver.switch_to.window(parent)
driver.quit()
