import random
import smtplib
import datetime as dt

my_mail = 'abcd2042002@gmail.com'
password = 'mghxzhzlsxbhduqv'

now = dt.datetime.now()
weekday = now.weekday()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2002, month=4, day=20)

if weekday == 5:
    with open("quotes.txt", encoding="utf8") as data_file:
        data = data_file.readlines()
        quotes = [value.replace("\n", "") for value in data]
        quote = random.choice(quotes)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_mail, password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs=my_mail,
                            msg=(f"Subject: Saturday Motivation\n\n{quote}").encode("utf-8").strip())
