##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime as dt

my_mail = 'abcd2042002@gmail.com'
password = 'hmtljavbaogfywoi'


# 1. Update the birthdays.csv

def update_birthtdays(name, email, year, month, day):
    new_birthday = {'name': name, 'email': email, 'year': year, 'month': month, 'day': day}
    row = pandas.DataFrame(new_birthday, index=[0])
    row.to_csv('birthdays.csv', mode='a', index=False, header=False)


# 2. Check if today matches a birthday in the birthdays.csv
with open("birthdays.csv") as data_file:
    birthdays = pandas.read_csv(data_file)

check_birthday = False
current_person = {}
now = dt.datetime.now()
# now = dt.datetime(year=2002, month=4, day=20)
for (index, row) in birthdays.iterrows():
    if row.day == now.day and row.month == now.month and row.year == now.year:
        current_person = row
        check_birthday = True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if check_birthday:
    index_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{index_letter}.txt") as data_letters:
        data = data_letters.read().replace("[NAME]", current_person['name'])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(my_mail, password)
            connection.sendmail(from_addr=my_mail,
                                to_addrs=current_person.email,
                                msg=(f"{data}").encode("utf-8").strip())

# 4. Send the letter generated in step 3 to that person's email address.
