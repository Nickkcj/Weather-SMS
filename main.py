import requests
from twilio.rest import Client

api_key = "cda7f0e2bc3e7e507b378f48c9559134" #Use your own api_key
account_sid = 'ACc480c80f3ae3bce92a7300967356fbd7' #Use your own account_sid
auth_token = '9df4a244bae5095ecb053586e4be3ea4' #Use your own auth_token
client = Client(account_sid, auth_token)

parameters = {
    "lat": -27.5954,
    "lon": -48.5480,
    "appid": api_key,
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
        from_='+13074413229',
        to='+5548998607422',
        body="It's going to rain today. Remember to bring an umbrella! ☔"
)
        
        print(message.status)
                
        

get_3hour_weather()
