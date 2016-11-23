from tree_node import Node
from queue import Queue


class Tree:
    def __init__(self, root_value=5):
        self.root = Node(root_value)
        self.node_count = 1
        self.level = 0

    def add_child(self, parent_value, child_value):
        parent = self.__find_node(self.root, parent_value)
        if parent is False:
            raise "No such value in tree."
        parent.add_child(child_value)
        if parent.get_last_child().level > self.level:
            self.level = parent.get_last_child().level
        self.node_count += 1

    def __find_node(self, root_node, x):
        if root_node.value == x:
            return root_node
        for child in root_node.get_children():
            res = self.__find_node(child, x)
            if res:
                return res
        return False

    def find(self, x):
        return bool(self.__find_node(self.root, x))

    def height(self):
        return self.level

    def count_nodes(self):
        return self.node_count

    def tree_levels(self):
        return [x for (_, x) in self.__tree_levels_with_bfs().items()]

    def __tree_levels_with_bfs(self):
        splicer = None  # this element will splice two levels in tree
        queue_ = Queue()

        queue_.push_back(self.root)
        queue_.push_back(splicer)  # level:0 from tree is only with the root

        levels = {0: [self.root.value], 1: []}
        level_cnt = 1

        while not(queue_.is_empty()):
            node = queue_.pop()
            if node == splicer:  # if we reach splicer: or the temp level is finished or the tree is already traversed
                if queue_.is_empty():  # tree is traversed
                    del levels[level_cnt]  # the last (key: value) is (level_cnt: []) - unneeded
                    return levels
                queue_.push_back(splicer)  # temp_level is finished - start new level
                level_cnt += 1
                levels[level_cnt] = []
            else:
                for child in node.get_children():
                    queue_.push_back(child)
                    levels[level_cnt].append(child.value)
        return levels

    def dfs_list(self):
        return Tree.traverse_dfs(self.root, [])

    @classmethod
    def traverse_dfs(cls, node, result):
        result.append(node.value)
        for child in node.get_children():
            Tree.traverse_dfs(child, result)
        return result
