import json
from panda import Panda
from graph import Graph
from panda_exeptions import PandaAlreadyThereError, PandasAlreadyFriendsError


class PandaSocialNetwork(Graph):
    def __init__(self):
        Graph.__init__(self)

    def has_panda(self, panda):
        if type(panda) is not Panda:
            raise TypeError("PandaSocialNetwork is for pandas!")
        return self.member(panda)

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThereError("This panda is already here.")
        self.add_isolated_vertex(panda)

    def make_friends(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriendsError("These pandas are already friends.")
        self.add_edge_between(panda1, panda2)

    def are_friends(self, panda1, panda2):
        return self.has_edge_between(panda1, panda2)

    def friends_of(self, panda):
        return self.get_neighbors_of(panda)

    def are_connected(self, panda1, panda2):
        return bool(self.shortest_path_between(panda1, panda2))

    def connection_level(self, panda1, panda2):
        path = self.shortest_path_between(panda1, panda2)
        if path:
            return len(path) - 1
        return -1

    def how_many_gender_in_network(self, level, panda, gender):
        level = self.nth_level_from_vertex(panda, level)
        count = 0
        for panda in level:
            if panda.gender() == gender:
                count += 1
        return count

    def save(self, file_name):
        PandaSocialNetwork.validate_file_name(file_name)
        json_objects = []
        for panda in self.graph:
            dict_obj = {"panda": panda.to_dict()}
            dict_obj["neighbors"] = [p.to_dict() for p in self.graph[panda]]
            json_objects.append(dict_obj)
        with open(file_name, 'w') as f:
            json.dump({"verticies": json_objects}, f, indent=8)

    @staticmethod
    def load(file_name):
        PandaSocialNetwork.validate_file_name(file_name)
        network = PandaSocialNetwork()
        f = open(file_name, 'r')
        data = json.load(f)
        for dict_obj in data["verticies"]:
            panda = Panda.create_from_dict(dict_obj["panda"])
            for dict_panda in dict_obj["neighbors"]:
                panda2 = Panda.create_from_dict(dict_panda)
                if not(network.are_friends(panda, panda2)):
                    network.make_friends(panda, panda2)
        f.close()
        return network

    @staticmethod
    def validate_file_name(file_name):
        if type(file_name) is not str:
            raise TypeError("Type of file name must be string.")
        if not(file_name.endswith(".json")):
            raise ValueError("File must be json file.")
