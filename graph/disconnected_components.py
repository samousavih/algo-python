from queue import LifoQueue
from dfs import dfs
from graph_adjacency_list import Graph


def disconnected_components(graph:Graph):
    components = []
    to_visit = LifoQueue()
    visited = set()
    current_component = []
    for node in graph.adjacency_list:
        if len(current_component) > 0:
            components.append(current_component)
            current_component = []
        if node not in visited:
            to_visit.put(node)
            current_component.append(node)
            while not to_visit.empty():
                current_node = to_visit.get()
                visited.add(current_node)
                for neighbor in graph.get_neighbors(current_node):
                    if neighbor not in visited:
                        to_visit.put(neighbor)
                        current_component.append(neighbor)
    return components

def is_valid_disconnected_components(graph:Graph, components):
    for index,component in enumerate(components):
        parents = dfs(graph,component[0])
        reachable_nodes = set()
        for p in parents:
            reachable_nodes.add(component[0])
            reachable_nodes.add(p)
        if reachable_nodes != set(component):
            return False
        for other_component in components[:index:]:
            if len(set(other_component).intersection(component)) >0 :
                return False
    return True
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


def test_connected_components():
    dg = get_test_graph_5()
    dg.show()

    components = disconnected_components(dg)
    assert(is_valid_disconnected_components(dg,components))


test_connected_components()