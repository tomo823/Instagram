#selenium==4.11.2

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
 
#browser Settings
driver = webdriver.Chrome()
driver.get("file:///C:/Users/xfura/Desktop/test.html")

#element_name = driver.find_element(By.XPATH, "/html/body/div/a")
#element_name.click()
follower_list = driver.find_element_by_css_selector("._a._a1._a2")
print(follower_list.text)