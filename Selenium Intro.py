from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chrome_service=r"C:\\Users\\DELL\\Desktop\\Selenium\\chromedriver-win64\\chromedriver-win64"
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/")
print(driver.title)