#latest selenium version is 4.11.2
#using selenium==3.141.0
#Succeeded to login

import time, csv, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import pyautogui

from get_profiles import get_filtered_profile, filter, filter_list

#make a directory and csv file for each user
search_name = "saya.ka2342"
userdir_path = os.path.join("..", "users_data", f"{search_name}")
if not os.path.exists(userdir_path):
    os.mkdir(userdir_path)
csv_path = os.path.join(userdir_path, f"{search_name}.csv")
kumamoto_csv_path = os.path.join(userdir_path, f"{search_name}_kumamoto.csv")

html_list = []
followers = []
filtered_followers = []

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

def move2followers(user):
    #fclick user column
    pyautogui.moveTo(30, 300)
    pyautogui.click()

    time.sleep(1.5)

    #move to username form
    pyautogui.moveTo(130, 235)
    pyautogui.click()

    time.sleep(1.5)

    #write username
    pyautogui.write(search_name)

    time.sleep(1.5)

    #click username
    pyautogui.moveTo(140, 290)
    pyautogui.click()

    time.sleep(2.5)

    #click followers list
    pyautogui.moveTo(760, 230)
    pyautogui.click()

    time.sleep(1.5)


def scrawl_followers():
    refresher = 0
    #scroll and display all followers
    while True:
        if refresher <= 2:
            driver.find_element_by_tag_name('body').click()
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        #delete last html
        if len(html_list) >= 3:
            html_list.pop(0)
            if html_list[0] == html_list[1]:
                print("Not updated")
                refresher += 1
            else:
                print("updated")
                refresher = 0
        
        if refresher >= 4:
            break
        html_list.append(driver.page_source)


def get_followers():
    #get followers list
    follower_list = driver.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")
    followers_list = []
    for followers in follower_list:
        followers_list.append(followers.text)

    #as confirmation
    print(followers_list)

    return followers_list


def write_csv(list):
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(list)


def write_filtered_csv(list):
    with open(kumamoto_csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        for follower in list:
            writer.writerow([follower])


if __name__ == "__main__":
    move2followers(search_name)
    scrawl_followers()
    followers = get_followers()
    write_csv(followers)
    filtered_followers = filter_list(followers)
    write_filtered_csv(filtered_followers)