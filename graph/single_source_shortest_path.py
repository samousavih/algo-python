
from queue import PriorityQueue, Queue
from weighted_graph_adjacency_list import WeightedGraph
import time


def single_source_shortest_path_with_min_heap(graph:WeightedGraph,source, dest):
    """
    min heap over regular queue is more efficient as takes less step
    O((E+V)LogV)
    """
    distance = {}
    tree = {}
    to_visit = PriorityQueue()
    for node in graph.get_nodes():
        distance[node] = float("INF") # O(V)
    tree[source] = None
    distance[source] = 0
    to_visit.put((0,source))
    i=0    
    while not to_visit.empty():
        _,next = to_visit.get() # O(VLogV)
        for neighbor,w in graph.get_neighbors(next):
            if distance[next] + w < distance[neighbor]:
                distance[neighbor]= distance[next] + w
                tree[neighbor] = next
                i+=1
                to_visit.put((distance[neighbor],neighbor)) #O(ELogV)
    print(f'steps wih min heap:{i}')
    node = dest
    path = []
    while node != None:
        path = [node] + path
        node = tree[node]

    return path,distance[dest]

def single_source_shortest_path_with_simple_queue(graph:WeightedGraph,source, dest):
    """
    """
    distance = {}
    tree = {}
    to_visit = Queue()
    for node in graph.get_nodes():
        distance[node] = float("INF")
    tree[source] = None
    distance[source] = 0
    to_visit.put((0,source))
    i = 0
    while not to_visit.empty():
        _,next = to_visit.get()
        for neighbor,w in graph.get_neighbors(next):
            if distance[next] + w < distance[neighbor]:
                distance[neighbor]= distance[next] + w
                tree[neighbor] = next
                i+=1
                to_visit.put((distance[neighbor],neighbor))
    print(f'steps wih queue:{i}')
    node = dest
    path = []
    while node != None:
        path = [node] + path
        node = tree[node]
    
    return path,distance[dest]



def test_single_source_shortest_path():
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
    # for testing negative cycles
    # g.insert_edge(1, 9, -5)
    # g.insert_edge(9, 7, -4)

    shortest_path,distance = single_source_shortest_path_with_min_heap(g, 0, 1)
    assert shortest_path == [0, 1] and distance == 4

    shortest_path,distance = single_source_shortest_path_with_simple_queue(g, 0, 1)
    assert shortest_path == [0, 1] and distance == 4

    start = time.time()
    shortest_path, distance = single_source_shortest_path_with_min_heap(g, 0, 8)
    end = time.time()
    print(end - start)
    assert shortest_path == [0, 1, 2, 3, 7, 8] and distance == 11
    start = time.time()
    shortest_path, distance = single_source_shortest_path_with_simple_queue(g, 0, 8)
    end = time.time()
    print(end - start)
    assert shortest_path == [0, 1, 2, 3, 7, 8] and distance == 11

    shortest_path, distance = single_source_shortest_path_with_min_heap(g, 5, 0)
    assert shortest_path == [5, 3, 2, 1, 0] and distance == 9

    shortest_path, distance = single_source_shortest_path_with_simple_queue(g, 5, 0)
    assert shortest_path == [5, 3, 2, 1, 0] and distance == 9

    shortest_path, distance = single_source_shortest_path_with_min_heap(g, 1, 1)
    assert shortest_path == [1] and distance == 0 

    shortest_path, distance = single_source_shortest_path_with_simple_queue(g, 1, 1)
    assert shortest_path == [1] and distance == 0 

test_single_source_shortest_path()

