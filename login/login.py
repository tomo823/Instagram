#Login into Instagram account

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


username    = "中西智哉"  # ユーザー名
password    = "tomo0427"   # パスワード


browser = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.instagram.com"
browser.get(url)
sleep(10)



# ログインフォームの要素取得
loginForm = browser.find_element_by_id("loginForm")

# ユーザー名入力
loginForm.find_element_by_name("username").send_keys(username)

# パスワード
loginForm.find_element_by_name("password").send_keys(password)

# ボタンクリック
btns = browser.find_elements_by_tag_name("button")
for i in btns:
    if i.text == 'Log In' or i.text == 'Log in':
        i.click()
        break
sleep(1)