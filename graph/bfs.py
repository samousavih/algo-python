from queue import Queue 
from graph_adjacency_list import get_test_graph_5,Graph

def bfs(graph:Graph,root):
    visited= {}
    parents = {}
    to_process = Queue()
    to_process.put(root)
    while not to_process.empty():
        current_node = to_process.get()
        if not current_node in visited or visited[current_node] == 0:
            visited[current_node] = 1
            process(current_node)
            for node in graph.adjacency_list[current_node]:
                to_process.put(node)
                parents[node] = current_node
    return parents
        
def process(node):
    print(f'{node} is processed')    


graph = get_test_graph_5()
parents = bfs(graph,3)       
print(parents)

