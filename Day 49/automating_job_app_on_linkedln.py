from json import load
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

load_dotenv()

USERNAME = os.environ["USER"]
PASSWORD = os.environ["PASSWORD"]

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

service = Service("./chorme-driver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=service, options=options)
driver.get(url=URL)

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button.click()

username_input = driver.find_element(By.XPATH, '//*[@id="username"]')
username_input.send_keys(USERNAME)

password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys(PASSWORD)

sign_in_button_2 = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button_2.click()

time.sleep(10)

# first_job = driver.find_element(By.XPATH, '//*[@id="ember232"]')
# first_job.click()
# time.sleep(2)
# easy_apply_button = driver.find_element(By.XPATH,
#                                         '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div')
# easy_apply_button.click()
# time.sleep(2)
#
# mobile_input = driver.find_element(By.XPATH,
#                                    '//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3305453706,71224597,phoneNumber~nationalNumber)"]')
# mobile_input.send_keys(PHONE_NUMBER)
#
# time.sleep(2)
#
# next_button = driver.find_element(By.CSS_SELECTOR, 'footer button')
# next_button.click()
#
# upload_resume = driver.find_element(By.CSS_SELECTOR,
#                                     '.jobs-easy-apply-form-section__grouping .js-jobs-document-upload__container label')
# upload_resume.click()
#
# next_button_2 = driver.find_element(By.CSS_SELECTOR, 'footer div.ph5.ph4').find_elements(By.TAG_NAME, 'button')[-1]
# next_button_2.click()

list_jobs = driver.find_elements(By.CSS_SELECTOR, 'ul.scaffold-layout__list-container li.ember-view')

for job in list_jobs:
    job_button = job.find_elements(By.CSS_SELECTOR, 'div > div')[0].find_elements(By.CSS_SELECTOR, 'div')[1]
    # print(first_job.get_attribute('innerHTML'))

    job_button.click()
    time.sleep(2)
    job_save_button = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
    job_save_button.click()
    time.sleep(2)

    dismis_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-toasts_toasts button')
    dismis_button.click()
    time.sleep(1)

    close_message_button = driver.find_elements(By.CSS_SELECTOR, '.msg-overlay-bubble-header__controls button')[2]
    close_message_button.click()
    time.sleep(2)
#
# follow_button = driver.find_element(By.CSS_SELECTOR,
#                                     '.jobs-search__job-details--container')
# print(follow_button.get_attribute('innerHTML'))
