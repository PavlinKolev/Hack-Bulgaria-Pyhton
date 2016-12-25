class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Pop from empty queue.")
        value_ = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = self.head
        self.size -= 1
        return value_
