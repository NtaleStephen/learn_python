students = [("Alice", 85), ("Bob", 72), ("Charlie", 78), ("Diana", 65)]

# write a python program to print the names of students who scored above 75

for student in students:
    name, score = student
    if score > 75:
        print(name)

# find the average score of the students
total_score = 0
for student in students:
    name, score = student
    total_score += score

average_score = total_score / len(students)
print(f"Average score: {average_score}")