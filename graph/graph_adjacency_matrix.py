adjacency_matrix = [[0 for x in range(10)] for y in range(10)]


def insert_edge(node1, node2):
    if adjacency_matrix[node1][node2] == 0: 
        adjacency_matrix[node1][node2] = 1
        adjacency_matrix[node2][node1] = 1
        return
    print(f"({node1},{node2}) alredy exists!")

def show():
    print(adjacency_matrix)


insert_edge(1,2)
insert_edge(2,3)
insert_edge(4,5)
insert_edge(5,4)
show()