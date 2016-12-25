from tree import Tree
from queue import Queue


class Graph:
    def __init__(self):
        self.graph = {}

    def add_isolated_vertex(self, vertex):
        if self.member(vertex):
            raise ValueError("This vertex is already in the graph.")
        self.graph[vertex] = []

    def add_edge_between(self, v1, v2):
        if self.has_edge_between(v1, v2):
            raise ValueError("There is already an edge between these vertices")
        if not(self.member(v1)):
            self.add_isolated_vertex(v1)
        if not(self.member(v2)):
            self.add_isolated_vertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def get_neighbors_of(self, vertex):
        if not(self.member(vertex)):
            return False
        return self.graph[vertex]

    def has_edge_between(self, v1, v2):
        if self.member(v1) and self.member(v2):
            return v2 in self.graph[v1]
        return False

    def shortest_path_between(self, v1, v2):
        bfs_tree = self.make_bfs_tree_from(v1)
        return bfs_tree.get_path_to(v2)

    def nth_level_from_vertex(self, vertex, level):
        if not(self.member(vertex)):
            raise ValueError("Vertex is not member in first_levels_from_vertex")
        bfs_tree = self.make_bfs_tree_from(vertex)
        return bfs_tree.nth_tree_level(level)

    def make_bfs_tree_from(self, vertex):
        if not(self.member(vertex)):
            raise ValueError("The vertex for bfs tree is not a member.")

        bfs_tree = Tree(vertex)
        visited = [vertex]

        splicer = None
        queue_ = Queue()

        queue_.push_back(vertex)
        queue_.push_back(splicer)

        while not(queue_.is_empty()):
            v = queue_.pop()
            if v is splicer:
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

    def member(self, vertex):
        return vertex in self.graph
