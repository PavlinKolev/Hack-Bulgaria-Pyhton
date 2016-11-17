class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.m_size = 0

    def __eq__(self, other):
        return LinkedList.equals(self.head, other.head)

    def add_element(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.m_size += 1

    def is_empty(self):
        return (self.head is None)

    def index(self, index):
        if index < 0 or index >= self.m_size:
            raise IndexError("Index out of range.")
        return LinkedList.iter_(self.head, index).value

    def size(self):
        return self.m_size

    def remove(self, index):
        if index < 0 or index >= self.m_size:
            raise IndexError("Index out of range.")
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = self.head
        else:
            prev_node = LinkedList.iter_(self.head, index - 1)
            prev_node.next = prev_node.next.next  # losing the link to the node we want to remove
            if prev_node.next is None:  # prev_node is the last elem
                self.tail = prev_node
        self.m_size -= 1

    def pprint(self):
        if self.is_empty():
            return ""
        return str(self.head.value) + LinkedList.str_list(self.head.next)

    def to_list(self):
        return LinkedList.nodes_to_list([], self.head)

    def add_at_index(self, index, data):
        if index < 0 or index > self.m_size:
            raise IndexError("Index out of range.")
        if index == 0:
            self.add_first(data)
        else:
            prev_node = LinkedList.iter_(self.head, index - 1)
            prev_node.next = Node(data, prev_node.next)
            self.m_size += 1

    def add_first(self, data):
        self.head = Node(data, self.head)
        if self.tail is None:
            self.tail = self.head
        self.m_size += 1

    def add_list(self, l: list):
        if not l:
            return
        self.add_element(l[0])
        l.pop(0)
        self.add_list(l)

    def add_nodes(self, node):
        if node is None:
            return
        self.add_element(node.value)
        self.add_nodes(node.next)

    def add_linked_list(self, ll):
        self.add_nodes(ll.head)

    def copy_to_ll(self,  node, count, temp_ll):
        if count is 0 or node is None:
            return temp_ll
        temp_ll.add_element(node.value)
        return self.copy_to_ll(node.next, count - 1, temp_ll)

    def ll_from_to(self, start_index, end_index):
        ll = LinkedList()
        count = end_index - start_index + 1
        return self.copy_to_ll(LinkedList.iter_(self.head, start_index), count, ll)

    def pop(self):
        self.remove(self.m_size - 1)

    def reduce_to_unique(self):
        if self.is_empty():
            return
        LinkedList.remove_repeats(self.head.next, self.head, [self.head.value])

    @classmethod
    def iter_(cls, node, pos):
        if pos == 0:
            return node
        return LinkedList.iter_(node.next, pos - 1)

    @classmethod
    def str_list(cls, node):
        if node is None:
            return ""
        return " -> " + str(node.value) + LinkedList.str_list(node.next)

    @classmethod
    def remove_repeats(cls, temp, prev, visited):
        if temp is None:
            return
        if temp.value in visited:
            prev.next = temp.next  # losing the link to the node we have to remove
        else:
            visited.append(temp.value)
            prev = temp
        LinkedList.remove_repeats(temp.next, prev, visited)

    @classmethod
    def equals(cls, node_1, node_2):
        if node_1 is None and node_2 is None:  # both reached the end node of lits
            return True
        if node_1 is None or node_2 is None:  # one reached the end before the other
            return False
        if node_1.value is not node_2.value:
            return False
        return LinkedList.equals(node_1.next, node_2.next)

    @classmethod
    def nodes_to_list(cls, temp_list, node):
        if node is None:
            return temp_list
        temp_list.append(node.value)
        return LinkedList.nodes_to_list(temp_list, node.next)
