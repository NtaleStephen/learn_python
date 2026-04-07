
from xml.dom import Node


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

root = Node("A")

child1  = Node("B")
child2  = Node("C")

root.children.append(child1)
root.children.append(child2)

print(root.value) # A
print(root.children[0].value) # B
print(root.children[1].value) # C

