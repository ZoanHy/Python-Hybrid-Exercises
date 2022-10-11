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
driver.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463")

# price = driver.find_element(By.CSS_SELECTOR, '#corePrice_desktop span.a-text-price span.a-offscreen').get_attribute('innerHTML')
price = driver.find_element(By.XPATH,
                            '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]').get_attribute(
    'innerHTML')

print(price)
