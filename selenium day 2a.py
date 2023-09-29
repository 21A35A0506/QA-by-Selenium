from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Use WebDriver manager to automatically download and manage ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
