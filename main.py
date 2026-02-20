# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

parameters = {
    "lat": 41.878113,
    "lon": -87.629799,
    "appid": API_KEY,
    "ctn": 4
}

url = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url, params=parameters)
weather_data = response.json()
will_rain = False

for item in range(len(weather_data["list"])):
    if int(weather_data["list"][item]["weather"][0]["id"]) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= "It's going to rain today. Bring ☔️.",
        from_="whatsapp:+14155238886",
        to="whatsapp:+818061792832"
    )
    print(message.status)
