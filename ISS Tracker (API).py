import requests
import datetime as dt
import smtplib
import time

my_email = "my_email@gmail.com"
my_password = "password"
my_latitude = "1.352083"
my_longtitude = "103.819839"

# Send a request to get the current position of ISS
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    # Check if current position is within +5 or -5 degrees of ISS position
    if my_latitude - 5 <= iss_latitude <= my_latitude + 5 and my_longtitude - 5 <= iss_longitude <= my_longtitude + 5:
        return True


# Send a request to get sunrise & sunset of current location
def is_night():
    parameters = {
        "lat": my_latitude,
        "lng": my_longtitude,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Get Sunrise, Sunset & Current hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour()
    # Check if its night-time
    if time_now <= sunrise or time_now >= sunset:
        return True


# Keep checking every 60s, if ISS is overhead & if its night-time, then send an email if both conditions are satisfied
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look Up☝🏻☝🏻\n\nThe ISS is above you right now!"
        )