# count how many even numbers are in a list 
numbers = [1,2,3,4,5,6,7,8,9,10]

even_count = 0

for num in numbers:
    if num %2 == 0:
        even_count += 1

print("Even numbers count: ", even_count)