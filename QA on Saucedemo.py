#verifying user details to access cart page
#created to ensure user can access the site without failures
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_service=Service("C:\\Users\\DELL\\Downloads\\chromedriver-win64")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/") #saucedemo can be used for quality testing
username=driver.find_element(By.ID,"user-name")
username.send_keys("standard_user")
password=driver.find_element(By.NAME,"password")
password.send_keys("secret_sauce")
login_btn=driver.find_element(By.XPATH,"//input[@id='login-button]")
login_btn.click()
cart=driver.find_element(By.CLASS_NAME,"shopping_cart_link")
if cart.is_displayed():
    print("user logged in")
else:
    print("unable to loggin")
product = driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]") 
product.click()
add_to_cart_btn = driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
add_to_cart_btn.click()
cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_link.click()
checkout_btn = driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']")
checkout_btn.click()
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Mayur")
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Vihar")
postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("12345")
continue_btn = driver.find_element(By.XPATH, "//input[@value='CONTINUE']")
continue_btn.click()
finish_btn = driver.find_element(By.XPATH, "//button[text()='FINISH']")
finish_btn.click()
confirmed=driver.find_element(By.CLASS_NAME,"payment_success")
if confirmed.is_displayed():
    print("You order successfully placed")
else:
    print("oops!Payment Failed")

