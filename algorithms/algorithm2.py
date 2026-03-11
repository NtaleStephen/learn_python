# a program that removes duplicates from a list
list = [1,2,3,4,2,5,6,7,7,6,8]

unique_list = []

for num in list:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)