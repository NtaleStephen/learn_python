# nums = [1,9,3,7,5]

# print(sorted(nums))


numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
    
print(numbers)
print("Largest: ", max(numbers))
print("Sum: ", sum(numbers))

print("sorted: ", sorted(numbers))
