#latest selenium version is 4.11.2
#using selenium==3.141.0
#Succeeded to login

import time, csv, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import pyautogui

#make a directory and csv file for each user
search_name = "203zhitian"
userdir_path = os.path.join("..", "users_data", f"{search_name}")
if not os.path.exists(userdir_path):
    os.mkdir(userdir_path)
csv_path = os.path.join(userdir_path,f"{search_name}.csv")

#browser Settings
driver = webdriver.Chrome(executable_path="C:\\Users\\xfura\\Desktop\\Instagram\\Instagram\\chromedriver.exe")
#opne instagram
driver.get("https://www.instagram.com")
driver.maximize_window()

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

time.sleep(6)

#find an account
pyautogui.moveTo(30, 300)
pyautogui.click()

time.sleep(1.5)

#move to followers
pyautogui.moveTo(130, 235)
pyautogui.click()

time.sleep(1.5)

pyautogui.write(search_name)

time.sleep(1.5)

pyautogui.moveTo(140, 290)
pyautogui.click()

time.sleep(1.5)

pyautogui.moveTo(760, 230)
pyautogui.click()

time.sleep(2)

#scroll and display all followers
last_height = driver.execute_script("return document.body.scrollHeight")
for i in range(40):
    driver.find_element_by_tag_name('body').click()
    #driver.execute_script("window.scrollTo(0, %d)" % last_top)
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)


#get followers list
follower_list = driver.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")
followers_list = []
for followers in follower_list:
    followers_list.append(followers.text)

#as confirmation
# print(followers_list)

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(followers_list)