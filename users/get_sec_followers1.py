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


class User:
    def __init__(self, name):
        self.name = name
        self.followers = []
        self.filtered_followers = []
        self.csv_path, self.kumamoto_csv_path = make_path(name)
        self.html_list = []

    def moveto_followers_list(self):
        #click the user column
        pyautogui.moveTo(30, 300)
        pyautogui.click()

        time.sleep(1.5)

        #move to username form
        pyautogui.moveTo(130, 235)
        pyautogui.click()

        time.sleep(1.5)

        #write username
        pyautogui.write(self.name)

        time.sleep(1.5)

        #click username
        pyautogui.moveTo(140, 290)
        pyautogui.click()

        time.sleep(2.5)

        #click followers list
        pyautogui.moveTo(760, 230)
        pyautogui.click()

        time.sleep(1.5)


    def scrawl_followers(self, refresher_th=3):
        #Initialize refresher
        refresher = 0
        long_html = False
        #scroll and display all followers
        while True:
            if refresher <= refresher_th:
                driver.find_element_by_tag_name('body').click()
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

            #delete last html if it's too long
            #FIXME: can use another variable to check if it's updated as boolean variable
            if len(html_list) >= 3:
                long_html = True
            
            if long_html:
                html_list.pop(0)
                if html_list[0] == html_list[1]:
                    print("Not updated")
                    refresher += 1
                else:
                    print("updated")
                    refresher = 0
            
            if refresher >= refresher_th + 1:
                break
            html_list.append(driver.page_source)

    
    def get_followers(self):
        #get followers list
        follower_list = driver.find_elements(By.CSS_SELECTOR, "._aacl._aaco._aacw._aacx._aad7._aade")
        followers_list = []
        for followers in follower_list:
            followers_list.append(followers.text)

        #as confirmation
        print(followers_list)

        return followers_list
    

    def write_csv(self, list):
        with open(self.csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(list)


    def write_filtered_csv(self, list):
        with open(self.kumamoto_csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            for follower in list:
                writer.writerow([follower])
    

class User_list:
    def __init__(self):
        self.user_list = []
    
    def append(self, user):
        self.user_list.append(user)
    
    def get_user(self, name):
        for user in self.user_list:
            if user.name == name:
                return user
        return None


#make a directory and csv file for each user
def make_path(name):
    userdir_path = os.path.join("..", "users_data", f"{name}")
    if not os.path.exists(userdir_path):
        os.mkdir(userdir_path)
    csv_path = os.path.join(userdir_path, f"{name}.csv")
    kumamoto_csv_path = os.path.join(userdir_path, f"{name}_kumamoto.csv")
    return csv_path, kumamoto_csv_path


#browser Settings
driver = webdriver.Chrome(executable_path="chromedriver.exe")
#open instagram
driver.get("https://www.instagram.com")
driver.maximize_window()


def login():
    #Login
    loginForm = driver.find_element_by_id("loginForm")
    loginForm.find_element_by_name("username").send_keys(username)
    loginForm.find_element_by_name("password").send_keys(password)
    loginButton = driver.find_element_by_css_selector("button[type=submit]")
    loginButton.click()


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



if __name__ == "__main__":
    html_list = []
    user_list = User_list()
    search_name = ["hdk_yuta0204"]
    for name in search_name:
        user = User(name)
        user_list.append(user)

    #User settings
    load_dotenv()
    username = os.getenv("MAIL")
    password = os.getenv("PASSWORD")

    time.sleep(0.4)
    login()
    time.sleep(6)

    for user in user_list.user_list:
        user.moveto_followers_list()
        user.scrawl_followers()
        user.followers = user.get_followers()
        user.write_csv(user.followers)
        user.filtered_followers = filter_list(user.followers)
        user.write_filtered_csv(user.filtered_followers)