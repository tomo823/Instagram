#latest selenium version is 4.11.2
#using selenium==3.141.0
#Succeeded to login

import time, csv, os, pathlib, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import pyautogui

current_dir = pathlib.Path(__file__).resolve().parent
parent_path = current_dir.parent
sys.path.append(os.path.join(parent_path, "users"))
from get_profiles import get_filtered_profile, filter, filter_list

csv_path = os.path.join("..", "users_data", "followers.csv")
kumamoto_csv_path = os.path.join("..", "users_data", "kumamoto_followers.csv")

#browser Settings
driver = webdriver.Chrome(executable_path="C:\\Users\\xfura\\Desktop\\Instagram\\Instagram\\chromedriver.exe")
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
loginForm = driver.find_element_by_id("loginForm")
loginForm.find_element_by_name("username").send_keys(username)
loginForm.find_element_by_name("password").send_keys(password)
loginButton = driver.find_element_by_css_selector("button[type=submit]")
loginButton.click()

time.sleep(4)

#move to profile
profileButton = driver.find_element_by_css_selector(r"a[href='/bizco_careerup/?next=%2F']")
profileButton.click()

time.sleep(1.5)

#move to followers
# followersButton = driver.find_element_by_css_selector(r"a[href='/bizco_careerup/followers/?next=%2F']")
# followersButton.click()
pyautogui.moveTo(760, 230)
pyautogui.click()

time.sleep(1.5)

#scroll and display all followers
#last_height = driver.execute_script("return document.body.scrollHeight")
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


#get followers list
follower_list = driver.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")
followers_list = []
for followers in follower_list:
    followers_list.append(followers.text)

#as confirmation
print(followers_list)

kumamoto_followers_list = filter_list(followers_list)

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(followers_list)

with open(kumamoto_csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(kumamoto_followers_list)