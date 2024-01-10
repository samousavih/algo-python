class Graph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        self.adjacency_list[data] = []
        self.number_of_nodes+=1

    def insert_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.adjacency_list[node1] = []
        if node2 not in self.adjacency_list:
            self.adjacency_list[node2] = []
        if node1 not in self.adjacency_list[node2]:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
            return
        print(f"Edge {node1} -> {node2} already exist!")


    def show(self):
        print(self.adjacency_list)

    def show_connections(self):
        for node in self.adjacency_list:
            print(f'{node} -->> {" ".join(map(str, self.adjacency_list[node]))}')


def get_test_graph_5():
    """
    Returns a graph with 3 cycles and 5 strongly connected components
    :return:
    """
    dg = Graph()
    dg.insert_edge(0, 2)
    dg.insert_edge(1, 3)
    dg.insert_edge(3, 2)
    dg.insert_edge(2, 1)
    dg.insert_edge(4, 5)
    dg.insert_edge(5, 6)
    dg.insert_edge(6, 4)
    dg.insert_edge(3, 5)
    dg.insert_edge(7, 5)
    dg.insert_edge(8, 10)
    dg.insert_edge(10, 11)
    dg.insert_edge(11, 9)
    dg.insert_edge(9, 8)
    return dg


def main():
    get_test_graph_5().show()       

if __name__ == "__main__":
    main()