import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

FACEBOOK = os.environ['FACEBOOK']
PASS = os.environ['PASSWORD']

URL = "https://tinder.com"
service = Service("./driver/chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
option.add_argument("start-maximized")
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=service, options=option)
driver.get(URL)

# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="t1452431810"]/div/div[2]/div/div/div[1]/div[1]/button/div[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="t1452431810"]/div/div[2]/div/div/div[1]/div[1]/button').click()

"""
    Login facbook
"""
time.sleep(2)
driver.find_element(By.XPATH,
                    '//*[@id="t1452431810"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/button').click()

time.sleep(2)
driver.find_element(By.XPATH,
                    '//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]').click()

base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)

time.sleep(2)
input_email = driver.find_element(By.ID, 'email')
input_email.send_keys(FACEBOOK)

time.sleep(2)
input_password = driver.find_element(By.ID, 'pass')
input_password.send_keys(PASS)
input_password.send_keys(Keys.ENTER)
time.sleep(2)
