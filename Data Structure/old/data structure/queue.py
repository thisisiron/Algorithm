class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items==[]

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())