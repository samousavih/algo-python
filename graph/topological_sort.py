from queue import LifoQueue
from directed_graph_adjacency_list import DirectedGraph

def topological_sort(graph:DirectedGraph):
    """
    Starts by calculating in degree of each node and then does a DFS starting with nodes with in degree 0.
    When discovering neighbors of a node decreases the in degree of them by one and continues the DFS for the ones with in degree 0.
    """

    visited = set()
    to_visit = LifoQueue()
    in_degree = {}
    sorted = []

    for node in graph.get_nodes():
        in_degree[node] = 0
    
    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            in_degree[neighbor]+=1
    for node in in_degree:
        if in_degree[node] == 0:
            to_visit.put(node) 
    while not to_visit.empty():
        current = to_visit.get()
        if current not in visited:
            visited.add(current)
            sorted.append(current)
            for node in graph.get_neighbors(current):
                in_degree[node]-=1
                if in_degree[node] == 0:
                    to_visit.put(node)

    return sorted

def get_test_graph_1():
    dg = DirectedGraph()
    dg.insert_edge(0, 1)
    dg.insert_edge(0, 5)
    dg.insert_edge(1, 2)
    dg.insert_edge(2, 4)
    dg.insert_edge(2, 6)
    dg.insert_edge(3, 2)
    dg.insert_edge(5, 8)
    dg.insert_edge(6, 5)
    dg.insert_edge(7, 5)
    return dg


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


graph1 = get_test_graph_1()
print(graph1.show())
print(topological_sort(graph1))

def is_valid_topological_sort(graph:DirectedGraph,sorted):
    index = 0
    for node in sorted:
        index+=1
        for neighbor in graph.get_neighbors(node):
            if neighbor in sorted[:index]:
                return False
    return True
def test_topological_sort():
    assert (is_valid_topological_sort(get_test_graph_1(),topological_sort(get_test_graph_1())))
    assert (is_valid_topological_sort(get_test_graph_2(),topological_sort(get_test_graph_2())))
    assert (is_valid_topological_sort(get_test_graph_3(),topological_sort(get_test_graph_3())))

test_topological_sort()

