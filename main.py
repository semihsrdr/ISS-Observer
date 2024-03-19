import requests
from datetime import datetime
import smtplib

my_latitude=41.015137
my_longitude=28.979530

my_email="blabla@gmail.com"
my_password="blabla"

my_parameters={
    "lat":my_latitude,
    "lng":my_longitude,
    "formatted":"0"
}

response_from_iss=requests.get("http://api.open-notify.org/iss-now.json")
response_from_iss.raise_for_status()
data=response_from_iss.json()
iss_latitude=float(data["iss_position"]["latitude"])
iss_longitude=float(data["iss_position"]["longitude"])

response_from_sun=requests.get("https://api.sunrise-sunset.org/json", my_parameters)
response_from_sun.raise_for_status()
sunrise=response_from_sun.json()['results']["sunrise"]
sunset=response_from_sun.json()['results']['sunset']

now=str(datetime.now()).split(" ")[1].split(".")[0].split(":")[0]
sunset=sunset.split("T")[1].split(":")[0]
sunrise=sunrise.split("T")[1].split(":")[0]

print(float(iss_latitude))
print(float(iss_longitude))

print(float(my_latitude))
print(float(my_longitude))

night=None
if now > sunrise and now < sunset:
    print("its a day")
    night=False
else:
    print("its a night")
    night=True

if night and iss_longitude-5>my_longitude>iss_longitude+5 and iss_latitude-5>my_latitude>iss_latitude+5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="smhserdarshn52@gmail.com",
                            msg=f"Subject:You Can See The ISS\n\n"
                                f"Hey, go and check the sky. International Space Station going "
                                f"over on your city.")