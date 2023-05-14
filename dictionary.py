dictionary = {
    "city": "Москва",
    "temperature": "20", 
    "country": "Russia"
}
print(dictionary['city'])
dictionary["temperature"] = int(dictionary["temperature"]) - 5
print(dictionary)

print(dictionary.get("country"))

dictionary['date'] = '14.05.2023'
print(dictionary)
print(len(dictionary))
