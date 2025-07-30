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
