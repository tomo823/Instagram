from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import os
from dotenv import load_dotenv
 
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome("Driver\\windows.exe")
driver.get('https://www.instagram.com')


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
profileButton = driver.find_element_by_css_selector(r"a[href='/bizco_careerup/']")
profileButton.click()

time.sleep(1.5)

#move to followers
followersButton = driver.find_element_by_css_selector(r"a[href='/bizco_careerup/followers/?next=%2F']")
followersButton.click()

time.sleep(1.5)

#scroll and display all followers
#last_height = driver.execute_script("return document.body.scrollHeight")
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
print(followers_list)

with open("followers.csv1", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(followers_list)