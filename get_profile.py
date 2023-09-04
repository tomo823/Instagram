import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import os
from dotenv import load_dotenv

#browser Settings
driver = webdriver.Chrome(executable_path="C:\\Users\\xfura\\Desktop\\Instagram\\Instagram\\login\\chromedriver.exe")
#opne instagram
driver.get("https://www.instagram.com")

#User settings
load_dotenv()
username = os.getenv("MAIL")
password = os.getenv("PASSWORD")

time.sleep(0.4)

#Login
loginForm = driver.find_element_by_id("loginForm")
loginForm.find_element_by_name("username").send_keys(username)
loginForm.find_element_by_name("password").send_keys(password)
loginButton = driver.find_element_by_css_selector("button[type=submit]")
loginButton.click()

time.sleep(4)