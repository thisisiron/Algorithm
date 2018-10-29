class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head==None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
        
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data, end=" => ")
            node = node.next
    
def main():
    l = LinkedList()
    l.add_at_front(3)
    l.add_at_front(5)
    l.add_at_end(7)
    l.print_list()


if __name__=="__main__":
    main()
