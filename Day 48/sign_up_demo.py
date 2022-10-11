from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chorme-driver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=service, options=options)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_address_input = driver.find_element(By.NAME, "email")
sign_up_button = driver.find_element(By.TAG_NAME, 'button')

first_name_input.send_keys("zoan")
last_name_input.send_keys("hy")
email_address_input.send_keys("huyleezoan@gmail.com")
sign_up_button.click()
