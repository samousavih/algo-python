"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""
from queue import PriorityQueue
def find_cheap_flight(flights,src,dst,k):
    
    distance = {}
    for node in get_nodes(flights):
        distance[node] = (float('inf'),float('inf'))
    distance[src] = (0,-1)
    to_visit = PriorityQueue()
    to_visit.put((0,src))
    tree = {}
    tree[src] = None
    while not to_visit.empty():
        _,current = to_visit.get()
        for next,w in get_neighbors(current,flights):
            dist_current,number_of_nodes_current = distance[current]
            dist_next,_ = distance[next]
            if number_of_nodes_current + 1 <= k and dist_next > dist_current + w:
                distance[next] = (dist_current + w,number_of_nodes_current + 1)
                to_visit.put((distance[next],next))
                tree[next] = current

    dist,number_of_nodes = distance[current]
    if dist == float('inf') or number_of_nodes > k:
        return -1
    return dist 


def get_neighbors(node,flights):
    neighbors = []
    for n in flights:
        if n[0] == node:
            neighbors.append((n[1],n[2]))
    return neighbors

def get_nodes(flights):
    nodes = set()
    for n in flights:
        nodes.add(n[0])
        nodes.add(n[1])
    return list(nodes)


def test_find_cheap_flight():
    assert find_cheap_flight([[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1) == 700
    assert find_cheap_flight([[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1) == 200
    assert find_cheap_flight([[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0) == 500


test_find_cheap_flight()