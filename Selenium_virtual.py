from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import urllib
import urllib.request
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BINARY')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

result = ''
result_name = ''
location = ''

# PREMADE PRESET
async def premade_process():
    global result
    global result_name
    global location

    # Opening Google on Chrome browser
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
    location = 'C:\\' + str(img_num) + '.png'
    img[img_num].screenshot(location)

async def delete():
    path = 'C:\\'
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if '.png' in f:
                os.remove(path + f)