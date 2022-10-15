import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

MAIL = os.environ['MAIL']
PASS = os.environ['PASSWORD']

URL = "https://tinder.com"

service = Service("../../../../../../ASUS/Documents/chromedriver.exe")
option = Options()
option.add_experimental_option("debuggerAddress", "localhost:9111")

os.popen(
    '"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9111 --user-data-dir="C:\\Users\ASUS\Documents"')

driver = webdriver.Chrome(executable_path="C:\\Users\ASUS\Documents\chromedriver.exe", options=option)
driver.maximize_window()
driver.get(URL)

# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="t1452431810"]/div/div[2]/div/div/div[1]/div[1]/button').click()
"""
    Login Google Account
"""

time.sleep(2)
login_button = driver.find_element(By.XPATH,
                                   '//*[@id="t1452431810"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

time.sleep(2)
google_button = driver.find_element(By.XPATH,
                                    '//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/div[1]/div/button/div[2]/div[2]')
google_button.click()

time.sleep(2)

base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)

time.sleep(2)
mail_input = driver.find_element(By.ID, 'identifierId')
mail_input.send_keys(MAIL)
mail_input.send_keys(Keys.ENTER)
