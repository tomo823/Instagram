#latest selenium version is 4.11.2
#using selenium==3.141.0
#urllib3==1.24.2
#Succeeded to login

import time, pyautogui, csv, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from dotenv import load_dotenv


#browser Settings
driver = webdriver.Chrome(executable_path=os.path.join("..", "chromedriver.exe"))
#open instagram
driver.maximize_window()
driver.get("https://www.instagram.com")


#User settings
load_dotenv()
username = os.getenv("MAIL")
password = os.getenv("PASSWORD")

user_list = []
with open('followers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        user_list.append(row)

#print(user_list[0])

time.sleep(1)

#Login
loginForm = driver.find_element_by_id("loginForm")
loginForm.find_element_by_name("username").send_keys(username)
loginForm.find_element_by_name("password").send_keys(password)
loginButton = driver.find_element_by_css_selector("button[type=submit]")
time.sleep(0.4)
loginButton.click()

time.sleep(4)

time.sleep(1)

#click for searching users
pyautogui.moveTo(40, 300, duration=0.25)
pyautogui.click()

time.sleep(0.4)

pyautogui.write(user_list[0][0])
pyautogui.moveTo(120, 320, duration=0.25)

time.sleep(0.4)
pyautogui.click()

