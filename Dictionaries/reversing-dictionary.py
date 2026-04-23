dict1 = {"name": "Ntale", "age": 30, "City": "Kampala"}

# Reversing the dictionary
reversed_dict = {}

for key, value in dict1.items():
    reversed_dict[value] = key
print(reversed_dict)


