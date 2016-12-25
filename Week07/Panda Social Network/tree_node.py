class TreeNode:
    def __init__(self, value, level=0):
        self.value = value
        self.children = []
        self.level = level

    def __str__(self):
        if self is None:
            raise TypeError("Cannot cast to string a none TreeNode!")
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def get_children(self):
        return self.children

    def add_child(self, child_value):
        self.children.append(TreeNode(child_value, self.level + 1))

    def get_children_count(self):
        return len(self.children)

    def is_leaf(self):
        return len(self.children) == 0

    def get_last_child(self):
        if self.is_leaf():
            raise IndexError("TreeNode doesnt have children.")
        return self.children[-1]
