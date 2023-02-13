dictionary = {
    "city": "Москва",
    "temperature": 20,
    "country": "Russia"
}
print(dictionary['city'])
dictionary["temperature"] = dictionary["temperature"] - 5
print(dictionary)

print(dictionary.get("date"))

dictionary['date'] = '12.03.2023'
print(dictionary)
print(len(dictionary))