import os
from tree import Tree


class FileTree(Tree):
    def __init__(self, path):
        Tree.__init__(self, path)
        for root, dirs, files in os.walk(path):
            node = self.find_node(self.root, str(root))
            for dir_ in dirs:
                node.add_child(os.path.join(root, dir_))
            for file_ in files:
                node.add_child(os.path.join(root, file_))
