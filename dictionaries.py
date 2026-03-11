# PersonalDetails = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 30,
#     "city": "New York"

# }

# PersonalDetails["age"] = 31

# PersonalDetails["email"] = "ntalestephen19@gmail.com"

# retreive = PersonalDetails.get("first_name")
# print(retreive)

student = {
    "name": "John",
    "age": 24,
    "course": "BCS"
    
}
# printing individual values inthe dictionary
print(student ["age"])
print(student ["course"])
print(student ["name"])


print(student)

# printing the value safely using get() method
print(student.get("age"))

print(student.keys())
print(student.values())

# USING items()
for key , value in student.items():
    print(key ,value)

# USING update() method
# this adds or modifies entries inside the dictionary
student.update({"age": 25})
# student["age"] = 20
print(student)

