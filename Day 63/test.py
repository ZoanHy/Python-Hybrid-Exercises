import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#  ---------- EDIT ----------
email = 'abcd2042002@gmail.com'  # replace email

password = 'password'  # replace password
#  ---------- EDIT ----------ok r đấy bạnh

# driver = uc.Chrome(executable_path="./driver/chromedriver.exe")
driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&continue=https://myaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button'
driver.get(url)

wait.until(EC.visibility_of_element_located(
    (By.NAME, 'identifier'))).send_keys(email)

sleep(4)

driver.execute_script(
    "document.querySelector('#identifierNext > div > button > div.VfPpkd-RLmnJb').click()")


# BẠN VIẾT THÊM CLICK BUTTON "Tiếp Theo" vào đây nhé
# wait.until(EC.visibility_of_element_located(
# By.ID, "identifierNext")).click()

wait.until(EC.visibility_of_element_located(
    (By.NAME, 'password'))).send_keys(password)

stop = input("stop to check result")
print("You're in!! enjoy")
sleep(10)

stop = input("stop to check result")
