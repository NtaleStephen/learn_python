# dictionary to store students and their marks and print the one with the highest mark

students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
}

top_student = ""
top_mark = 0

for name, mark in students.items():
    if mark > top_mark:
        top_mark = mark
        top_student = name in students.items()

