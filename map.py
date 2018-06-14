import sys

class Map_node:
    def __init__(self, node_id, name="", prosperity=100):
        self.node_id = node_id
        if name == "":
            self.name = str(self.node_id)
        else:
            self.name = name
        self.neighbor_nodes = []
        self.prosperity = prosperity
        self.ruler = None
