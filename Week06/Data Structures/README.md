# Data Structures

## Linked List

We already know what is the Linked List Data Structure.

A sequence of data structures( which we called 'Nodes'), which are connected together via links. Each Node has data( doens't matter what is
the content of that data) and a link to the next Node.

We implemented the following methods to our Linked List:

```python
def add_element(self, data): pass
def set_element(self, index, data): pass
def index(self, index): pass
def size(self): pass
def remove(self, index): pass
def pprint(self): pass
def to_list(self): pass
# add element and index N (Example: ll = [2 => 3 => 4]
# ll.ad_at_index(1, "New data")
# ll = [2 => "New data" =>  3 => 4]
def add_at_index(self, index, data): pass
def add_first(self, data): pass
def add_list(self, lst): pass
def add_linked_list(self, ll): pass
def ll_from_to(self, start_index, end_index): pass
def pop(self): pass
def reduce_to_unique(self): pass
```

# Now it is time to learn what is stack, queue and tree

## Stack (LIFO)

This Data Structure is named stack, because behaves like a real-world stack, for example – a deck of cards or a pile of plates, etc. Each element in the stack is again a Node(which has only data, no link to the next Node). The last element in the stack is the first one popped when we want to iterate over the structure.

Methods we can apply on:

```python
def push(self, data): pass # Pushing (storing) an element on the stack. In Python we can use stack.append(element)
def pop(self): pass # Removing (accessing) an element from the stack.
def peek(self): pass # get the top data element of the stack, without removing it.
def is_empty(self): pass # check if stack is empty.
```

## Queue (FIFO)

This Data Structure is named queue, because behaves like a real-world queue, for example – a queue in the shop, etc. Each element in the queue is again a Node(which has only data, no link to the next Node). The first element in the queue is the first one popped when we want to iterate over the structure.

Methods we can apply on:

```python
def push(self, data): pass # Pushing (storing) an element on the queue. Append!
def pop(self): pass # Removing (accessing) an element from the queue. In Python - queue.popleft() !
def peek(self): pass # get the top data element of the queue, without removing it.
def is_empty(self): pass # check if queue is empty.
```

## Tree

Today we will learn that kind of structure is the Tree.

Data Structure, which has a main Node, called root. This Node has `n` number of children. The parent of those children is the root. Each child has its own children and etc. The last children of the tree are called leaves.

Important: Each child is the root of its own tree!

Your task for today is to implement the main methods to work with the Tree data structure. We need generic Tree where each node can have different number of children.

```python
class Tree:
  def __init__(self, root):
    pass
    """
    When we are creating a new tree, we must always have a root element.
    For example:
    tree = Tree(root=5)
    """

  def add_child(self, parent, child):
    pass
    """
    When we are adding new element to our tree, we must specify the parent:
    tree = Tree(root=5)
    tree.add(parent=5, child=4)
    tree.add(parent=5, child=3)
    tree.add(parent=4, child=2)

    This will make the following tree:

        5
       / \
      4   3
     /
    2
    """

  def find(self, x):
    pass
    """
        Returns True or False if Node with value x is present in the tree
    """

  def height(self):
    pass
    """
        Returns an integer number of the max height of the tree
          5
         / \
        4   3
       /
      2

      tree.height() = 2
    """

  def count_nodes(self):
    pass
    """
        Returns the number of node sin the tree
        In our example -> tree.count_nodes() = 4
    """

  def tree_levels(self):
    pass
    """
        Returns a list of lists with the nodes foe each level1
        tree.tree_levels = [[5], [4, 3], [2]]
    """



```

