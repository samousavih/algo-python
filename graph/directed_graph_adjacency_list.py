import copy

class DirectedGraph():
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def insert_node(self, data):
        self.adjacency_list[data] = []
        self.number_of_nodes+=1

    def insert_edge(self, node1, node2):
        if node1 not in self.adjacency_list:
            self.insert_node(node1)
        if node2 not in self.adjacency_list:
            self.insert_node(node2)
        if node2 not in self.adjacency_list[node1]:
            self.adjacency_list[node1].append(node2)
            return
        print(f"Edge {node1} -> {node2} already exist!")
    
    def get_nodes(self):
        return self.adjacency_list.keys()
    def get_neighbors(self,node):
        return self.adjacency_list[node]



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
    dg = DirectedGraph()
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

def get_test_graph_1():
    udg = DirectedGraph()
    udg.insert_edge(0, 1)
    udg.insert_edge(1, 2)
    udg.insert_edge(2, 3)
    udg.insert_edge(1, 7)
    udg.insert_edge(3, 7)
    udg.insert_edge(7, 8)
    udg.insert_edge(3, 4)
    udg.insert_edge(3, 5)
    udg.insert_edge(4, 5)
    udg.insert_edge(5, 6)
    udg.insert_edge(6, 7)
    udg.insert_edge(6, 8)

    return udg

def get_test_graph_2():
    dg_small = DirectedGraph()
    dg_small.insert_edge(2, 1)
    dg_small.insert_edge(4, 5)
    dg_small.insert_edge(0, 1)
    dg_small.insert_edge(1, 4)
    dg_small.insert_edge(1, 3)

    return dg_small


def get_test_graph_3():
    dg_other = DirectedGraph()
    dg_other.insert_edge(3, 11)
    dg_other.insert_edge(5, 2)
    dg_other.insert_edge(2, 4)
    dg_other.insert_edge(2, 7)
    dg_other.insert_edge(8, 11)
    dg_other.insert_edge(4, 7)
    dg_other.insert_edge(7, 8)

    return dg_other


def get_test_graph_4():
    """
    Returns graph containing a cycle
    :return:
    """
    dg = copy.copy(get_test_graph_1())
    dg.insert_edge(8, 0)  # creates cycle

    return dg



def main():
    get_test_graph_5().show()       

if __name__ == "__main__":
    main()