import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

TARGET_PRICE = 100
my_mail = 'abcd2042002@gmail.com'
password = 'mghxzhzlsxbhduqv'

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

params_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

reponse = requests.get(url=URL, headers=params_header)

soup = BeautifulSoup(reponse.text, 'lxml')

price = float(soup.select_one(selector="#corePrice_desktop span.a-text-price span.a-offscreen").getText().split('$')[1])
product_name = soup.find(id="productTitle").getText().strip().split(',')[0]

if price > TARGET_PRICE:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_mail, password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs=my_mail,
                            msg=(f"Subject: Amazon Price Alear!\n\n{product_name}: ${price}").encode("utf-8"))
