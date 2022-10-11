import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chorme-driver/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=service, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, "cookie")

total_cookies = driver.find_element(By.ID, "money")

time_machine_select = driver.find_element(By.ID, "buyTime machine")
portal_select = driver.find_element(By.ID, "buyPortal")
alchemy_lab_select = driver.find_element(By.ID, "buyAlchemy lab")
shipment_select = driver.find_element(By.ID, "buyShipment")
mine_select = driver.find_element(By.ID, "buyMine")
factory_select = driver.find_element(By.ID, "buyFactory")
grandma_select = driver.find_element(By.ID, "buyGrandma")
cursor_select = driver.find_element(By.ID, "buyCursor")

five_seconds = time.time() + 5
five_minutes = time.time() + 60 * 5

# while True:
#     cookie_button.click()
#
#     if time.time() > timeout:
all_prices_tag = driver.find_elements(By.CSS_SELECTOR, '#store b')
prices = []

for tag in all_prices_tag:
    prices.append(tag.get_attribute('innerHTML').split(" ")[-1].replace(',', ''))

# money = int(total_cookies.get_attribute('innerHTML'))
# portal_cost = int(
#     portal_select.find_element(By.TAG_NAME, 'b').get_attribute('innerHTML').split(" ")[-1].replace(',', ''))
# alchemy_cost = int(
#     alchemy_lab_select.find_element(By.TAG_NAME, 'b').get_attribute('innerHTML').split(" ")[-1].replace(",", ''))
#
# shipment_cost = int(
#     shipment_select.find_element(By.TAG_NAME, 'b').get_attribute('innerHTML').split(" ")[-1].replace(',', ''))
# mine_cost = int(
#     mine_select.find_element(By.TAG_NAME, 'b').get_attribute('innerHTML').split(" ")[-1].replace(',', ''))
# factory_cost = int(
#     factory_select.find_element(By.TAG_NAME, 'b').get_attribute('innerHTML').split(" ")[-1].replace(',', ''))
# grandma_cost = int(
#     grandma_select.find_element(By.TAG_NAME, 'b').get_attribute('innerHTML').split(" ")[-1].replace(',', ''))
# cursor_cost = int(
#     cursor_select.find_element(By.TAG_NAME, 'b').get_attribute('innerHTML').split(" ")[-1].replace(',', ''))

# currsor_run()
