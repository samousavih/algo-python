adjacency_map = []

def insert_edge(node1, node2):
    if (node1,node2) not in adjacency_map: 
        adjacency_map.append((node1,node2))
        adjacency_map.append((node2,node1))
        return
    print(f"({node1},{node2}) alredy exists!")

def show():
    print(adjacency_map)


insert_edge(1,2)
insert_edge(2,3)
insert_edge(4,5)
insert_edge(5,4)
show()