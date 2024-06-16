from smtplib import *

my_email = "my_email@gmail.com"
my_password = "password"
receipient_email = "receipient_email@gmail.com"

with SMTP("smtp.gmail.com") as connection:
    connection.starttls() # To make the connection secure
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=receipient_email, msg="Subject:Hello \n\nThis is to place the content of email.")

 