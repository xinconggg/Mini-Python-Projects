import datetime as dt
import smtplib
import random

my_email = "my_email@gmail.com"
my_password = "password"
now = dt.datetime.now()
day_of_week_now = now.weekday()

# If today is Monday then randomly choose a quote from "quotes.txt"
if day_of_week_now == 0: 
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp@gmail.com") as connection:
        connection.starttls() # To ensure that the connection is secure
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Monday Motivational Quotes \n\n{quote}")