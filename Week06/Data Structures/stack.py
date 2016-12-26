class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail = Node(value, self.tail)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise "Empty Queue."
        value_ = self.tail.value
        self.tail = self.tail.next
        if self.tail is None:
            self.head = self.tail
        self.size -= 1
        return value_

    def peek(self):
        if self.is_empty():
            raise "Empty Queue."
        return self.tail.value
