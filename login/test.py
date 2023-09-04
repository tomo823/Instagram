#selenium==4.11.2

import time, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pathlib

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
print(chrome_options.binary_location)
#print(sys.path)