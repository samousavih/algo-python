from graph_adjacency_list import Graph


def is_bipartite(graph:Graph):
    node_color = {}
    to_visit = []
    to_visit.append(graph.get_nodes()[0])
    node_color[graph.get_nodes()[0]] = 0
    while len(to_visit) > 0:
        node = to_visit.pop()
        for neighbor in graph.get_neighbors(node):
            if neighbor in node_color:
                if node_color[neighbor] == node_color[node]:
                    return False
            else:
                node_color[neighbor] = 1 - node_color[node]
                to_visit.append(neighbor)
    return True



def get_test_graph_1():
    udg = Graph()
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
    udg = Graph()
    udg.insert_edge(0, 1)
    udg.insert_edge(0, 5)
    udg.insert_edge(2, 1)
    udg.insert_edge(2, 3)
    udg.insert_edge(2, 5)
    udg.insert_edge(4, 3)
    udg.insert_edge(4, 5)
    udg.insert_edge(4, 7)
    udg.insert_edge(6, 7)

    return udg


def test_bipartite():
    # udg = get_test_graph_1()
    # assert(is_bipartite(udg) == False)

    udg2 = get_test_graph_2()
    assert (is_bipartite(udg2) == True)
test_bipartite()