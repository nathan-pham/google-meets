from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import time
import random

from options import opt
from classes import *

driver = webdriver.Chrome(options=opt) 

def join(code):
  driver.get(f"https://meet.google.com/{code}")
  time.sleep(10)
  driver.find_element_by_css_selector('span.NPEfkd').click()

