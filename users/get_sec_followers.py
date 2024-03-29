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
from sup import run_elevated_powershell_command, change_ip_address



class User:
    def __init__(self, name):
        self.name = name
        self.followers = []
        self.filtered_followers = []
        self.csv_path, self.kumamoto_csv_path = make_path(name)
        self.html_list = []


    def moveto_followers_list(self, user_count):
        #click the user column
        pyautogui.moveTo(30, 300)
        pyautogui.click()
        time.sleep(1)

        # if user_count == 2:
        #     pyautogui.moveTo(620, 560)
        #     pyautogui.click()
        #     time.sleep(1.5)

        #     pyautogui.moveTo(30, 300)
        #     pyautogui.click()
        #     time.sleep(2.5)         

        #move to username form
        pyautogui.moveTo(130, 235)
        pyautogui.click()
        time.sleep(0.5)

        #write username
        pyautogui.write(self.name)
        time.sleep(1)

        #click username
        pyautogui.moveTo(170, 290)
        pyautogui.click()
        time.sleep(2.5)

        #click followers list
        pyautogui.moveTo(760, 230)
        pyautogui.click()
        time.sleep(1.5)


    def scrawl_followers(self, refresher_th=1):
        #Initialize refresher
        refresher = 0
        long_html = False

        #scroll and display all followers
        pyautogui.moveTo(822, 586)
        while True:
            if refresher <= refresher_th:
                pyautogui.click()
            pyautogui.scroll(-1000)
            time.sleep(2)

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
            
            if refresher >= refresher_th:
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



def login():
    #Login
    loginForm = driver.find_element_by_id("loginForm")
    loginForm.find_element_by_name("username").send_keys(username)
    loginForm.find_element_by_name("password").send_keys(password)
    loginButton = driver.find_element_by_css_selector("button[type=submit]")
    loginButton.click()


#make a directory and csv file for each user
def make_path(name):
    userdir_path = os.path.join("..", "users_data", f"{name}")
    if not os.path.exists(userdir_path):
        os.mkdir(userdir_path)
    csv_path = os.path.join(userdir_path, f"{name}.csv")
    kumamoto_csv_path = os.path.join(userdir_path, f"{name}_kumamoto.csv")
    return csv_path, kumamoto_csv_path


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
    pyautogui.write(user)

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
    #broanesis.recruit_shiowser Settings
    driver = webdriver.Chrome("chromedriver.exe")
    #open instagram
    driver.get("https://www.instagram.com")
    driver.maximize_window()

    html_list = []
    user_count = 0

    #Initialize names for search
    search_names = [["hdk_yuta0204"]]
    # search_names_path = os.path.join("..", "users_data", "kumamoto_followers.csv")
    # with open(search_names_path, 'r') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         search_names.append(row)

    #Initialize user_list
    user_list = User_list()
    
    length_list= len(search_names[0])
    for name in search_names[0]:
        #Initialize user, creating directory and csv file
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
        print(f"\nSearching followers for User: {user.name}\n")
        user.moveto_followers_list(user_count)
        user.scrawl_followers()
        temp_followers = user.get_followers()
        user.write_csv(temp_followers)

        #insert followers list into user.followers, but maximum length is 120 per 1 element
        n = 1
        finish = False
        while True: #if length of temp_followers is less than 120, just insert temp_followers into user.followers
            if len(temp_followers) < 120:
                user.followers.append(temp_followers)

                finish = True
            else: #if length of temp_followers is more than 120, insert first 120 followers into user.followers
                user.followers.append(temp_followers[:n * 120])
                temp_followers = temp_followers[n * 120:]
                n += 1

            try: #filter users, insert into user.filtered_followers and clear user.followers
                print(f"Filtering followers for User: {user.name}")
                temp1_list = filter_list(user.followers)
                user.followers = []
                if finish:
                    break
                #change ip address
                change_ip_address()

            except: #in case of blocking error
                driver.close()
                break
        
        #output filter followers list
        user.write_filtered_csv(user.filtered_followers)

        #In case of multiple users
        if length_list > 1:
            pyautogui.moveTo(805, 235)
            pyautogui.click()

        #In case of pop-up
        user_count += 1
    
    #close browser
    driver.close() if driver.window_handles else None
    driver.quit()