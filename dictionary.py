weather_dict = {
    "city": "Москва",
    "temperature": "20", 
    "country": "Russia"
}
print(weather_dict['city'])
weather_dict["temperature"] = str(int(weather_dict["temperature"]) - 5)
print(weather_dict)

print(weather_dict.get("country"))

weather_dict["date"] = "14.05.2023"
print(weather_dict)
print(len(weather_dict))
