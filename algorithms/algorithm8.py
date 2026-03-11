# create a a simple student grade system

marks = [85,73,60,45,90]

for mark in marks:
    if mark >= 80:
        grade = "A"

    elif mark >= 70:
        grade = "B"

    elif mark >= 60:
        grade = "C"

    else:
        grade = "D"

    print(f"Mark: {mark}, Grade: {grade}")
