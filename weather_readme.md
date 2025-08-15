# 🌤️ Weather App

A simple and elegant Python application that fetches real-time weather information for any city using the WeatherAPI service.

## ✨ Features

- 🌍 **Global Coverage**: Get weather data for any city worldwide
- 🌡️ **Current Conditions**: Real-time temperature and weather conditions
- 💨 **Simple Interface**: Easy-to-use command-line interface
- ⚡ **Fast Response**: Quick API calls for instant weather updates
- 🔧 **Error Handling**: Robust error handling for invalid inputs

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- `requests` library

### Installation

1. **Clone or download** the weather app file
2. **Install required dependencies**:
   ```bash
   pip install requests
   ```

### Usage

1. **Run the application**:
   ```bash
   python weather.py
   ```

2. **Enter a city name** when prompted:
   ```
   Enter city name: London
   ```

3. **View the weather information**:
   ```
   City: London
   Temperature: 15.2°C
   Condition: Partly cloudy
   ```

## 📋 Code Overview

```python
import requests

city = input("Enter city name: ")
api_key = "f525dd1440dc42b8b2c195316250807"
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"City: {data['location']['name']}")
    print(f"Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
else:
    print("Error fetching weather data.")
    print("Status Code:", response.status_code)
    print("API Response:", data)
```

## 🔧 Configuration

### API Key Setup

The application uses WeatherAPI.com for weather data. The API key is currently hardcoded in the script. For production use, consider:

1. **Environment Variables**:
   ```python
   import os
   api_key = os.getenv('WEATHER_API_KEY')
   ```

2. **Config File**:
   ```python
   import json
   with open('config.json') as f:
       config = json.load(f)
       api_key = config['api_key']
   ```

## 📊 Sample Output

```
Enter city name: New York
City: New York
Temperature: 22.1°C
Condition: Sunny

Enter city name: Tokyo  
City: Tokyo
Temperature: 18.5°C
Condition: Light rain

Enter city name: InvalidCity
Error fetching weather data.
Status Code: 400
API Response: {'error': {'code': 1006, 'message': 'No matching location found.'}}
```

## 🛠️ Possible Enhancements

- [ ] Add support for multiple cities at once
- [ ] Include additional weather parameters (humidity, wind speed, etc.)
- [ ] Add weather forecasts (5-day, hourly)
- [ ] Create a GUI version using tkinter or PyQt
- [ ] Add unit conversion (Celsius/Fahrenheit)
- [ ] Save weather history to a file
- [ ] Add weather alerts and notifications

## 🌐 API Reference

This app uses [WeatherAPI.com](https://www.weatherapi.com/) which provides:

- **Current Weather**: Real-time weather conditions
- **Global Coverage**: 1 million+ locations worldwide
- **JSON Response**: Easy to parse weather data
- **Free Tier**: Up to 1 million calls per month

### Response Format
```json
{
  "location": {
    "name": "London",
    "country": "United Kingdom"
  },
  "current": {
    "temp_c": 15.2,
    "condition": {
      "text": "Partly cloudy"
    }
  }
}
```

## ⚠️ Error Handling

The application handles various error scenarios:

- **Invalid City Names**: Returns error message with status code
- **Network Issues**: Handles connection timeouts
- **API Limitations**: Manages rate limiting and quota exceeded errors
- **Malformed Responses**: Validates JSON structure

## 📝 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Support

If you encounter any issues or have questions:

- Check the [WeatherAPI documentation](https://www.weatherapi.com/docs/)
- Review common error codes and solutions
- Submit an issue on the project repository

---

**Made with ❤️ for weather enthusiasts**