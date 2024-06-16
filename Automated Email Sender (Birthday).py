import datetime as dt
import smtplib
import pandas as pd
import random

my_email = "my_email@gmail.com"
my_password="password"

# Create a tuple consisting of today's month & day
now = dt.datetime.now()
month_now = now.month
day_now = now.day
today = (month_now, day_now)

# Check if today matches a birthday in "birthdays.csv" then choose a letter randomly out of the 3 available & send an email to the person
data = pd.read_csv("birthdays.csv")
for (index, data_row) in data.iterrows():   # Create a birthday dictionary
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter = f"letter_{random.randint(1,3)}.txt"
    # Replace "[NAME]" in the letters to name of the birthday person
    with open(letter) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])
    # Send to birthday person's email
    with smtplib.SMTP("smtp@gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")