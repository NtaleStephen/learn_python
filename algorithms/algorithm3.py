# a program to calculate the sum and average of a list of numbers
scores = (70,80,85,90,95)

total = sum(scores)
average = total / len(scores)
print("Total: ", total)
print("Average: ", average)


scores1 = (10,30,50,56)

total = 0

for score in scores1:
    total += score

average = total / len(scores1)
print("Total: ", total)
print("Average: ", average)