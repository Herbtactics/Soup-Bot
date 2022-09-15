from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import urllib
import urllib.request
import os
import pyautogui
from knownpaths import *

# What does soup bot do:

# Take inputs from discord chat (i.e. chicken, noddle)
# string = ""

# # Add inputs into a list
# input_list = []
# input_list.append(string)

# # Compile them into a single string variable
# single_string = ""
# for index in range(0, len(list)):
#     single_string += (list[index] + " ")

# Put the variable into a Google images search tab
    # Opening Google on Chrome browser

def find(name,path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

PATH = find("chromedriver.exe", 'C:\\')
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com/imghp?hl=en&ogbl")
driver.maximize_window()

    # Putting variable into search bar
search = driver.find_element(By.NAME, "q")
search.send_keys("chicken noodle soup") # Replace with single_string
search.send_keys(Keys.RETURN)

# Takes a random image and gets its url
picture_number = random.randint(1, 10)
img = driver.find_elements(By.CLASS_NAME, "rg_i")
img_num = 0
if len(img) < 10:
    img_num = random.randint(0, len(img))
else:
    img_num = random.randint(0, 9)
img[img_num].click()
test = []
img_jpg = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.CLASS_NAME, "v4dQwb")))
for img in img_jpg:
    test.append(img.get_attribute('src'))
print(test)
# img_jpg = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "v4dQwb")))
# img_link = img_jpg.get_attribute('src')
# print(img_link)

#|----------------------------------------------------------------------------------------------------------|



# # Download the image
# pyautogui.hotkey("ctrl", "s")
# time.sleep(1)
# pyautogui.press("enter")

# time.sleep(10)

# path = get_path(FOLDERID.Downloads)
# downloads = os.listdir(path)

# # for items in downloads:

# list = []
# for (root, dirs, file) in os.walk(path, topdown=True):
#     for f in file:
#         if '.html' in f:
#             list.append(f)

    
#|----------------------------------------------------------------------------------------------------------|

# maybe... ---^