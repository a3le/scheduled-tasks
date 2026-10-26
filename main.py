# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas as pd
import random
import smtplib
import os

# import os and use it to get the Github repository secrets

birthday = pd.read_csv('./birthdays.csv')
#conver the day from a range of 0 - 6 using map and replace on the birthdays['day'] series
today = dt.datetime.now()
today_date = today.day
today_month = today.month


MY_EMAIL = os.environ.get("email")
MY_PASSWORD = os.environ.get("password")

#reciver email address
email_reciver = 'addadh898@outlook.com'

#chosing all the rows with this specific day
birthday = birthday[(birthday['day'] == today.day) & (birthday['month'] == today_month)]
#converting the rows to dictonary to work on it
birthday = birthday.to_dict(orient='records')

for x in birthday:
    if len(birthday) > 0:
        name = x['name']
        with open(f'./letter_templates/letter_{random.randint(1,3)}.txt') as letter_file:
            letter_msg = letter_file.readlines()
            new_msg = [msg.replace('[NAME],\n', f'{name},\n') for msg in letter_msg]
            new_msg = [msg.replace('Angela', 'Sami\n') for msg in new_msg]
            message = ''.join(new_msg)

            connection = smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email_reciver, msg=f"Subject: Birthday\n\n {new_msg}")


