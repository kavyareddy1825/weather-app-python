import requests

API_KEY = "d1beebbee5a54bac43dfe79bb4ec75b1"

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
print(data)
if data["cod"] != "404":
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\nWeather in", city)
    print("Temperature:", temp, "°C")
    print("Condition:", weather)
    print("Humidity:", humidity, "%")
else:
    print("City not found!")