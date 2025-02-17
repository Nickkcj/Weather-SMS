import requests
from twilio.rest import Client


client = Client(account_sid, auth_token)

parameters = {
    "lat": -27.5954,
    "lon": -48.5480,
    "appid": "",
    "cnt": 4
}


def get_3hour_weather():
    response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)
    if response.status_code == 200:
        data = response.json()
        will_rain = False
        for hour_data in data['list']:
            if hour_data['weather'][0]['id'] < 700:
                will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='',
        to='',
        body="It's going to rain today. Remember to bring an umbrella! ☔"
)
        
        print(message.status)
                
        

get_3hour_weather()
