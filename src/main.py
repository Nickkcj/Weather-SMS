from src.api.weather_api import fetch_weather
from src.notifications.sms_notification import send_sms

def main():
    lat = -27.5954
    lon = -48.5480

    try:
        weather_data = fetch_weather(lat, lon)
        will_rain = any(
            hour['weather'][0]['id'] < 700 for hour in weather_data['list']
        )
        
        if will_rain:
            status = send_sms("It's going to rain today. Remember to bring an umbrella! ☔")
            print(f"SMS sent with status: {status}")
        else:
            print("No rain expected today.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
