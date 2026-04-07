from collections import deque 

queue = deque("HELLO")

list1 = list(queue)

print(list1)

word = "HELLO"

for char in word:
    queue.append(char)

print(queue)