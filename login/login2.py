#chromedriver_binary==115.0.5790.170.0

import time
import chromedriver_binary
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#WEBブラウザの起動
driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')
time.sleep(2)

username = "ビズコ|25卒就活部"
password = "tomo0427"
# Usernameを入力
usernameInput = driver.find_element_by_name(username)
usernameInput.send_keys(username)
# Passwordを入力
passwordInput = driver.find_element_by_css_selector("input[name=password]")
passwordInput.send_keys(password)

"""browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.instagram.com/accounts/login/"
browser.get(url)

loginForm = browser.find_element_by_id("loginForm")

loginForm.find_element_by_name("username").send_keys(username)"""