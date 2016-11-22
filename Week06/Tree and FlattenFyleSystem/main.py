from flattens import flatten
from flattens import *
from tree import Tree

def main1():
    tree = Tree()
    tree.add_child(5, 4)
    tree.add_child(5, 3)
    tree.add_child(4, 2)
    tree.add_child(3, 6)
    tree.add_child(2, 1)
    levels = tree.tree_levels()
    print(levels)
    print(tree.count_nodes())
    print(tree.height())

def main2():
    for root, dirs, files in os.walk("/home/pavcho/101Python/week03"):
        print("Root: ",  root)
        print(" Dirs: ------------------")
        for dir in dirs:
            print("     ", dir)
        print(" Dirs files --------------")

        print(" Files: ------------------")
        for file in files:
            print("     ", file)
        print(" End files --------------")

def main4():
    p = flatten([[5, 6, 7], 1, 2, [8, 9]])
    print(p)
    # py ../week06/Tree/main.py


def main3():
    path = "/home/pavcho/101Python/week03"
    l_1 = flatten_file_system1(path)
    l_2 = flatten_file_system2(path)

    for elem in l_1:
        print(elem)
    print ("\n\nPutkaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n")
    for elem in l_2:
        print(elem)

def main5():
    t = Tree()
    t.add_child(5, 1)
    t.add_child(5, 2)
    t.add_child(1, 4)
    t.add_child(1, 6)
    t.add_child(5, 3)
    t.add_child(3, 8)
    t.add_child(3, 9)
    t.add_child(2, 7)
    res = t.my()
    print(res)



if __name__ == '__main__':
    main3()
