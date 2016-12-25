from tree import Tree
from queue import Queue


class Graph:
    def __init__(self):
        self.graph = {}

    def add_isolated_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge_between(self, v1, v2):
        if self.are_two_vertexes_connected(v1, v2):
            raise ValueError("There is already an edge between these vertexes")
        if not(self.__member(v1)):
            self.add_isolated_vertex(v1)
        if not(self.__member(v2)):
            self.add_isolated_vertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def get_neighbors_of(self, vertex):
        if not(self.__member(vertex)):
            return False
        return self.graph[vertex]

    def are_two_vertexes_connected(self, v1, v2):
        return v2 in self.graph[v1]

    def shortest_path_between(self, v1, v2):
        bfs_tree = self.make_bfs_tree_from(v1)
        return bfs_tree.get_path_to(v2)

    def make_bfs_tree_from(self, vertex):
        if not(self.__member(vertex)):
            raise ValueError("The vertex for bfs tree is not a member.")

        bfs_tree = Tree(vertex)
        visited = [vertex]

        splicer = None
        queue_ = Queue()

        queue_.push_back(vertex)
        queue_.push_back(splicer)

        while not(queue_.is_empty()):
            v = queue_.pop()
            if v == splicer:
                if queue_.is_empty():
                    return bfs_tree
                queue_.push_back(splicer)
            else:
                for neighboor in self.graph[v]:
                    if neighboor not in visited:
                        bfs_tree.add_child(v, neighboor)
                        queue_.push_back(neighboor)
                        visited.append(neighboor)
        return bfs_tree

    def __member(self, vertex):
        return vertex in self.graph
