from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "./chorme-driver/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

service = Service("./chorme-driver/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

"""
    Get infor from amazaon
"""
# driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")

# price = driver.find_element(By.CSS_SELECTOR, '#corePrice_desktop span.a-text-price span.a-offscreen').get_attribute('innerHTML')
# price = driver.find_element(By.XPATH,
#                             '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]').get_attribute(
#     'innerHTML')
#
# print(price)

"""
    Get infor from python.org
"""

driver.get("https://www.python.org/")

ul_upcoming_tag = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

events = ul_upcoming_tag.find_elements(By.TAG_NAME, 'a')
times = ul_upcoming_tag.find_elements(By.TAG_NAME, 'time')

event_dict = {}

for i in range(len(events)):
    event = events[i].get_attribute('innerHTML')
    time = times[0].get_attribute('datetime').split("T")[0]
    event_dict[i] = {
        'time': time,
        'name': event
    }

