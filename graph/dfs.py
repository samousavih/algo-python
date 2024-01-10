from queue import LifoQueue 
from graph_adjacency_list import get_test_graph_5,Graph

def dfs(graph:Graph,root):
    visited= set()
    parents = {}
    to_process = LifoQueue()
    to_process.put(root)
    while not to_process.empty():
        current_node = to_process.get()
        if not current_node in visited:
            visited.add(current_node)
            process(current_node)
            for node in graph.adjacency_list[current_node]:
                to_process.put(node)
                parents[node] = current_node
    return parents
        
def process(node):
    print(f'{node} is processed')    

def dfs_recursive(graph:Graph,root,visited= set(),parents = {}):
    if root not in visited:
        process(root)
        visited.add(root)
        for node in graph.adjacency_list[root]:
            parents[node] = root
            dfs_recursive(graph,node,visited,parents)
    return parents


graph = get_test_graph_5()
graph.show()
parents = dfs(graph,3)
print(f"Dfs with stack : {parents}")
parents = dfs_recursive(graph,3)
print(f"Dfs recursive : {parents}")       


