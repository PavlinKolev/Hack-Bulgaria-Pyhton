from file_tree import FileTree


def flatten_file_system1(path):
    file_tree = FileTree(path)
    tree_levels = file_tree.tree_levels()
    return flatten(tree_levels)


def flatten_file_system2(path):
    file_tree = FileTree(path)
    return file_tree.dfs_list()


def flatten(list_):
    res = []
    for elem in list_:
        if type(elem) is list:
            res += flatten(elem)
        else:
            res += [elem]
    return res
