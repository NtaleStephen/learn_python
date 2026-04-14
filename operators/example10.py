# Mixed Operators (Exam Standard)
# Task

# Write a program that:

# Takes a number
# Checks:
# If it is even
# If it is greater than 10
# Prints True only if both conditions are satisfied
# Solution

num = int(input("Enter a number: "))

is_even = num % 2 == 0

is_greater_than_10 = num > 10

print("Both conditions satisfied:", is_even and is_greater_than_10)

