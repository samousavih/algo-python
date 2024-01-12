class WeightedGraph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        self.adjacency_list[data] = []
        self.number_of_nodes+=1

    def insert_edge(self, node1, node2, w):
        if node1 not in self.adjacency_list:
            self.insert_node(node1)
        if node2 not in self.adjacency_list:
            self.insert_node(node2)
        if node1 not in self.adjacency_list[node2]:
            self.adjacency_list[node1].append((node2,w))
            self.adjacency_list[node2].append((node1,w))
            return
        print(f"Edge {node1} -> {node2} already exist!")
    
    def get_neighbors(self,node):
        return self.adjacency_list[node]
    
    def get_nodes(self):
        return list(self.adjacency_list.keys())

    def show(self):
        print(self.adjacency_list)

    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')