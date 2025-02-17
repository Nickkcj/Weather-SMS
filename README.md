# ☔ Weather SMS Service

This project uses the `requests` and `twilio` Python modules to notify you via SMS when rain is expected in the next 12 hours based on your location (longitude and latitude).

---

## 🌟 Features

- Fetches weather forecast data using the OpenWeatherMap API.
- Detects rain conditions in the forecast.
- Sends an SMS reminder to bring an umbrella using Twilio.

---

## 📦 Dependencies

- `requests` (for making API calls to OpenWeatherMap)
- `twilio` (for sending SMS notifications)

---

## ⚙️ Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Nickkcj/Weather-SMS.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - OpenWeatherMap: Create an account and get your API key.
   - Twilio: Create an account and get your `account_sid` and `auth_token`.

4. Update the configuration in the code:
   - Replace placeholders with your API keys and Twilio credentials.

---

## 📄 Usage

1. Run the `main.py` script:
   ```bash
   python src/main.py
   ```

2. If rain is expected in the next 12 hours, you will receive an SMS reminder to bring an umbrella!

---

## 🌐 API References

- **OpenWeatherMap API**: [https://openweathermap.org/api](https://openweathermap.org/api)
- **Twilio API**: [https://www.twilio.com/docs/usage/api](https://www.twilio.com/docs/usage/api)

---
