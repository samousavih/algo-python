from queue import PriorityQueue
from weighted_graph_adjacency_list import WeightedGraph


def minimum_spanning_tree(g:WeightedGraph):
    """
    The key to understanding this algo is always we want to find a node which has the lowest weighted edge from the tree.
    "if w < weight_from_tree[node]:" this condition is for optmisation as if we already know the distance from tree to node N is W and then
    we found another edge which reach us to N which has a weight larger than W so we don't need to add that into the min heap. 
    """
    min_heap = PriorityQueue()
    parent = {}
    zero = g.get_nodes()[0]
    weight_from_tree = {}
    parent[zero] = None
    for node in g.get_nodes(): #O(V)
        weight_from_tree[node] = float("inf") 
    for node,w in g.get_neighbors(zero):
        min_heap.put((w,(zero,node))) # O(E)
        weight_from_tree[node] = w
    while not min_heap.empty():
        _,(s, t) = min_heap.get()
        if t not in parent and s in parent:
            parent[t] = s
            for node,w in g.get_neighbors(t):
                if node not in parent:
                    if w < weight_from_tree[node]: 
                        weight_from_tree[node] = w
                        min_heap.put((w,(t,node)))

    return parent



def get_graph_1():
    g = WeightedGraph()
    g.insert_edge(0, 1, 4)
    g.insert_edge(1, 7, 6)
    g.insert_edge(1, 2, 1)
    g.insert_edge(2, 3, 3)
    g.insert_edge(3, 7, 1)
    g.insert_edge(3, 4, 2)
    g.insert_edge(3, 5, 1)
    g.insert_edge(4, 5, 1)
    g.insert_edge(5, 6, 1)
    g.insert_edge(6, 7, 2)
    g.insert_edge(6, 8, 2)
    g.insert_edge(7, 8, 2)
    return g

def get_graph_2():
    g = WeightedGraph()
    g.insert_edge("a", "b", 4)
    g.insert_edge("b", "c", 8)
    g.insert_edge("c", "d", 7)
    g.insert_edge("b", "h", 11)
    g.insert_edge("a", "h", 8)
    g.insert_edge("h", "i", 7)
    g.insert_edge("i", "c", 2)
    g.insert_edge("i", "g", 6)
    g.insert_edge("c", "f", 4)
    g.insert_edge("d", "f", 14)
    g.insert_edge("d", "e", 9)
    g.insert_edge("e", "f", 10)
    g.insert_edge("g", "f", 2)
    g.insert_edge("h", "g", 1)
    return g



def test_mst():
    msp = minimum_spanning_tree(get_graph_1())
    print(msp)
    assert(msp == {0: None, 1: 0, 2: 1, 3: 2, 5: 3, 7: 3, 4: 5, 6: 5, 8: 7})
    msp = minimum_spanning_tree(get_graph_2())
    assert(msp == {'a': None, 'b': 'a', 'h': 'a', 'g': 'h', 'f': 'g', 'c': 'f', 'i': 'c', 'd': 'c', 'e': 'd'})
    print(msp)

test_mst()