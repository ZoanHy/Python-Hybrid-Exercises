from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

service = Service("./chorme-driver/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(total_articles.get_attribute('innerHTML'))
# total_articles.click()

all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
# all_portals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python")
search.send_keys(Keys.ENTER)
