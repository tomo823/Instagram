#latest selenium version is 4.11.2
#using selenium==3.141.0
#Succeeded to login

import time, csv, os, sys
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from pathlib import Path

parent_dir = Path(__file__).resolve().parent
second_parent_dir = parent_dir.parent
sys.path.append(os.path.join(second_parent_dir, "users"))

from get_profiles import get_filtered_profile, filter, filter_list

csv_path = os.path.join("..", "users_data", "followers.csv")
kumamoto_csv_path = os.path.join("..", "users_data", "kumamoto_followers.csv")

#browser Settings
driver = webdriver.Chrome()
#opne instagram
driver.get("https://www.instagram.com")

time.sleep(0.4)
driver.maximize_window()

#User settings
load_dotenv()
username = os.getenv("MAIL")
password = os.getenv("PASSWORD")

time.sleep(0.4)

#Login
loginForm = driver.find_element(By.ID, "loginForm")
loginForm.find_element(By.NAME, "username").send_keys(username)
loginForm.find_element(By.NAME, "password").send_keys(password)
loginButton = driver.find_elements(By.TAG_NAME, "button")
loginButton[1].click()

time.sleep(8)

#move to profile
profileButton = driver.find_element(By.CSS_SELECTOR, r"a[href='/bizco_careerup/?next=%2F']")
profileButton.click()

time.sleep(5)

#move to followers
pyautogui.moveTo(760, 210)
pyautogui.click()

time.sleep(1.5)

#scroll to display all followers
pyautogui.moveTo(822, 586)
pyautogui.click()
refresher = 0
long_html = False
html_list = []
while True:
    if len(html_list) >= 3:
        long_html = True
    #driver.find_element_by_tag_name('body').click()
    #driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    pyautogui.scroll(-1000)
    time.sleep(2)

    if len(html_list) >= 3:
        long_html = True
    
    if long_html:
        html_list.pop(0)
        if html_list[0] == html_list[1]:
            refresher += 1
            
        else:
            refresher = 0
    
    if refresher >= 3:
        break
    html_list.append(driver.page_source)

time.sleep(1.5)

#get followers list
follower_list = driver.find_elements(By.CSS_SELECTOR, "._ap3a._aaco._aacw._aacx._aad7._aade")
followers_list = []
for followers in follower_list:
    followers_list.append(followers.text)

#as confirmation
# print(followers_list)

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(followers_list)

#Filter the list
kumamoto_followers_list = filter_list(followers_list)

with open(kumamoto_csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(kumamoto_followers_list)