# function to count items in a list

# def count_items(items):

#     count = 0

#     for item in items:
#         count += 1
#         print("total items: ", count)


# fruits = ["apple", "banana", "mango"]

# count_items(fruits)


# fruits = ["apple", "banana", "mango", "orange", "grape"]

# def count_items(items):

#     count = 0

#     for item in items:
#         count +=1

#     print("Total items: ", count)

# count_items(fruits)


def count_items(items):

    count = 0
    
    for item in items:
        count +=1 
    return count


fruits = ["apple", "banana", "mango", "orange", "grape"]

total = count_items(fruits)
print("Total items: ", total)