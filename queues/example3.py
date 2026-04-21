class  Queue:
    def __init__(self):
        self.queue = []

    def  enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue underflow"

        return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return None
        

        return self.queue[0]
    
    def is_empty(self):
        return self.queue == []
    
    def size(self):
        return len(self.queue)

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.front())
print(q.size())

print(q.dequeue())

print(q.front())
print(q.size())
