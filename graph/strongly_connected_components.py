from queue import LifoQueue
from dfs import dfs
from directed_graph_adjacency_list import DirectedGraph

def dfs_reverse(graph:DirectedGraph,root):
    visited= set()
    parents = {}
    to_process = LifoQueue()
    to_process.put(root)
    parents[root] = root
    while not to_process.empty():
        current_node = to_process.get()
        if not current_node in visited:
            visited.add(current_node)
            for node in graph.get_inverse_neighbors(current_node):
                to_process.put(node)
                if node not in parents:
                    parents[node] = current_node
    return parents

def is_strongly_connected(graph:DirectedGraph):
    nodes = list(graph.get_nodes())
    tree = dfs(graph,nodes[0])
    if len(tree) != len(nodes):
        return False
    reverse_tree = dfs_reverse(graph,nodes[0])
    if len(reverse_tree) != len(nodes):
        return False
    return True


def strongly_connected_components(graph:DirectedGraph):
    visited = set()
    finished_stack = []
    to_visit_stack = []
    components =[]
    for node in graph.get_nodes():
        if node not in visited:
            to_visit_stack.append(node)
            while len(to_visit_stack) > 0:
                current_node = to_visit_stack.pop()
                if current_node in visited:
                    finished_stack.append(current_node)
                else :
                    visited.add(current_node)
                    to_visit_stack.append(current_node)
                for neighbor in graph.get_neighbors(current_node):
                    if neighbor not in visited:
                        to_visit_stack.append(neighbor)
    visited = set()
    to_visit_stack = []
    component=[]
    while len(finished_stack) > 0 :
        if len(component) > 0:
            components.append(component)
            component = []
        node = finished_stack.pop()
        if node not in visited:
            to_visit_stack.append(node)
            while len(to_visit_stack) > 0:
                current_node = to_visit_stack.pop()
                visited.add(current_node)
                component.append(current_node)
                for neighbor in graph.get_inverse_neighbors(current_node):
                    if neighbor not in visited:
                        to_visit_stack.append(neighbor)
    
    return components

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


def test_connected_components():
    dg = get_test_graph_5()
    dg.show()

    assert(is_strongly_connected(dg) == False)

def test_strongly_connected_components():
    dg = get_test_graph_5()

    components = strongly_connected_components(dg)
    assert (components == [[8, 9, 11, 10], [7], [0], [2, 3, 1], [5, 4, 6]])


test_connected_components()
test_strongly_connected_components()