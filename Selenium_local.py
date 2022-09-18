from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import urllib
import urllib.request
import os
import pyautogui
import re

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

result = ''
result_name = ''

# PREMADE PRESET
async def premade_process():
    global result
    global result_name

    # Opening Google on Chrome browser
    def find(name,path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    PATH = find("chromedriver.exe", 'C:\\')
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.google.com/imghp?hl=en&ogbl")
    driver.maximize_window()

    # Getting variables
    meat = ['egg', 'chicken', 'beef', 'lamb']
    # vegetables = ['brocolli']
    # broth = []
    # seasoning = []
    select = random.randint(0,len(meat) - 1)
    ingredient = meat[select]
    result_name = str(ingredient)

    # Putting variable into search bar
    search = driver.find_element(By.NAME, "q")
    search.send_keys(ingredient) # Replace with single_string
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

    action = ActionChains(driver)
    right_side_pic = driver.find_elements(By.CLASS_NAME, "eHAdSb")
    for index in range(0, len(right_side_pic)):
        try:
            action.context_click(right_side_pic[index]).perform()
        except:
            continue
        else:
            time.sleep(0.2)
            for times in range(0,3):
                pyautogui.hotkey("up")
            time.sleep(1)
            pyautogui.hotkey("enter")

    # enter url back into search bar
    search = driver.find_element(By.NAME, "q")
    search.clear()
    search.click()
    pyautogui.hotkey("ctrl","v")
    search.send_keys(Keys.RETURN)

    # get url value/link
    search = driver.find_element(By.NAME, "q")
    paste = search.get_attribute('value')

    # if url value is not jpg repeat function
    match = re.search(r'.jpg', str(paste))
    if match:
        print('jpg')
        result = str(paste)
        return result
        driver.quit()
    else:
        print('not jpg')
        result = str(paste)
        print(result)
        driver.close()
        await premade_process()

# CUSTOM PRESET
async def custom_process():
    global result
        
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

    action = ActionChains(driver)
    right_side_pic = driver.find_elements(By.CLASS_NAME, "eHAdSb")
    for index in range(0, len(right_side_pic)):
        try:
            action.context_click(right_side_pic[index]).perform()
        except:
            continue
        else:
            time.sleep(0.2)
            for times in range(0,3):
                pyautogui.hotkey("up")
            time.sleep(1)
            pyautogui.hotkey("enter")

    # enter url back into search bar
    search = driver.find_element(By.NAME, "q")
    search.clear()
    search.click()
    pyautogui.hotkey("ctrl","v")
    search.send_keys(Keys.RETURN)

    # get url value/link
    search = driver.find_element(By.NAME, "q")
    paste = search.get_attribute('value')

    # if url value is not jpg repeat function
    match = re.search(r'.jpg', str(paste))
    if match:
        print('jpg')
        result = str(paste)
        return result
    else:
        print('not jpg')
        custom_process()
