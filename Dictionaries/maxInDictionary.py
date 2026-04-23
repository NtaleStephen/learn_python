dict = {"a": 5, "b": 10, "c": 3}

max_value = max(dict.values())
max_key = max(dict, key=dict.get)
print(f"The maximum value in the dictionary is: {max_value}")
print(f"The key with the maximum value is: {max_key}")