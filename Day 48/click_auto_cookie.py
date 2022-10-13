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

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

five_seconds = time.time() + 5
five_minutes = time.time() + 60 * 5

while True:
    cookie_button.click()

    if time.time() > five_seconds:
        all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        prices = []

        for tag in all_prices:
            element_text = tag.get_attribute('innerHTML')
            if element_text != "":
                prices.append(
                    int(element_text.split(" ")[-1].replace(',', '')))

        cookie_upgrade = {}
        for n in range(len(prices)):
            cookie_upgrade[prices[n]] = item_ids[n]

        money_current = driver.find_element(By.ID, "money").get_attribute('innerHTML')
        if "," in money_current:
            money_current = money_current.replace(",", "")
        cookie_count = int(money_current)

        affordable_upgrades = {}

        for cost, id in cookie_upgrade.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price = max(affordable_upgrades)

        to_purchase_id = affordable_upgrades[highest_price]

        driver.find_element(By.ID, to_purchase_id).click()
        timeout = time.time() + 5

    if time.time() > five_minutes:
        cookie_per = driver.find_element(By.ID, "cps").get_attribute('innerHTML')
        print(cookie_per)
        break
