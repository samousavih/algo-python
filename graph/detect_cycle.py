from queue import LifoQueue
from directed_graph_adjacency_list import DirectedGraph, get_test_graph_1, get_test_graph_2, get_test_graph_3, get_test_graph_4, get_test_graph_5


def detect_cycle(graph: DirectedGraph):
    """
    If the key is from a finished node in DFS there is an edge to a visited node there is a cycle. So we need to track the status of a node during DFS.
    If for a node all of it's children have been finished that node is finished too. To achieve it each time we visit a node we put that back on stack and the second time we
    see that node is finished.
    """
    VISITED = 1
    PROCESSED = 2
    status = {}
    stack = LifoQueue()


    # 1---->2----->3
    # 2----->4---->3

    # 1----->2--->3---->2
    
    for node in graph.get_nodes():
        stack.put(node)
        while not stack.empty():
            to_visit = stack.get()
            if to_visit not in status:
                status[to_visit] = VISITED
                stack.put(to_visit)
            else :
                status[to_visit] = PROCESSED
            for neighbor in graph.get_neighbors(to_visit):
                if neighbor in status and status[neighbor] == VISITED:
                    print(f'cycle detected in {neighbor} and parent: {to_visit}')
                    return True
                stack.put(neighbor)
    return False




def test_detect_cycle():
    assert (detect_cycle(get_test_graph_5()) == True)
    assert (detect_cycle(get_test_graph_1()) == False)
    assert (detect_cycle(get_test_graph_2()) == False)
    assert (detect_cycle(get_test_graph_3()) == False)
    assert (detect_cycle(get_test_graph_4()) == True)
get_test_graph_5().show()
test_detect_cycle()    