class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items==[]

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def print_stack(self):
        print(self.items)


s = Stack()
s.push('1')
s.push('2')
s.push('3')
s.print_stack()

s.pop()
s.print_stack()