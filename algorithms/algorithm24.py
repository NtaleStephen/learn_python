# function to find the largest number in the list, sum of the numbers and sorted list

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print("Largest number:", largest)


nums = [4, 9, 2, 7, 5]
find_largest(nums)

