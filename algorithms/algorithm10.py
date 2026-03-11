# count items greater than 40 in a list

list = [20,30,40,50,60]

count = 0

for num in list:
    if num > 40:
        count += 1

print("Count of numbers greater than 40: ", count)


numbers = [1,2,3,4,5,6,7,8,9,10]

count1 = 0

for num1 in numbers:
    if num1 % 2 ==0:
        count1 += 1
print("Count of even numbers: ", count1)

# count number of elements in the list
list1 = [1,2,3,4,5,6,7,8,9,10]

count2 = 0

for num2 in list1:
    count2 += 1
print("Count of numbers in the list: ", count2)