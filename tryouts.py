# solution 1
numbers = []

for i in range(5):
    num = int(input("enter a number: "))
    numbers.append(num)

summation = sum(numbers)
print("SUM: ", summation)

average = (summation)/len(numbers)

print(average)

# solution 2
word = input("Enter a word: ")

print("Length of the word: ", len(word))

numbers = []

for i in range(3):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("smallest: ", min(numbers))


# solution 3
numbers = []
for i in range(4):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("sort: ", sorted(numbers, reverse=True))

# solution 4
num = int(input("Enter a number: "))
print(abs(num))

# solution 1
numbers = []

for i in range(5):
    num = int(input("enter a number: "))
    numbers.append(num)

summation = sum(numbers)
print("SUM: ", summation)

average = (summation)/2

print(average)

# solution 2
word = input("Enter a word: ")

print("Length of the word: ", len(word))

numbers = []

for i in range(3):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("smallest: ", min(numbers))


# solution 3
numbers = []
for i in range(4):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("sort: ", sorted(numbers))

# solution 4
num = int(input("Enter a number: "))
print(abs(num))

# solution 5
while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. try again.")
