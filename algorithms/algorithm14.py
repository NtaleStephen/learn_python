# print all students names and their ages

students = {
    "John" : 20,
    "Alice" : 22,
    "Bob" : 19,
    "Charlie" : 21
}

for name, age in students.items():
    print(name, "is", age, "years old")