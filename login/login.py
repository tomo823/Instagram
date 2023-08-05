#selenium==4.11.2
#Succeeded to login

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
#browser Settings
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")

time.sleep(2)

#login Settings
username = "bizco.st44@gmail.com"
password = "bizco4455"

#Input Username
element_name = driver.find_element(By.NAME, "username")
element_name.send_keys(username)

#Input Password
element_pass = driver.find_element(By.NAME, "password")
element_pass.send_keys(password)

#Submitting form
element_submit = driver.find_element(By.ID, "loginForm")
element_submit.submit()