dictionary = {
    "Uganda": "Kampala",
    "Kenya": "Nairobi",
    "Tanzania": "Dodoma",
    "Rwanda": "Kigali",
    "sudan" :"Khartoum"

}

sorting = sorted(dictionary.keys())
print(sorting)

addingNewItem = dictionary["Uganda"] = "Entebbe"
print(dictionary)

removingItem = dictionary.pop("sudan")
print(dictionary)