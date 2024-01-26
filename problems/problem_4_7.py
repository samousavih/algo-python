"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c 
"""

from queue import Queue


def build_order(projects,dependencies):
    in_degree = {}
    for project in projects:
        in_degree[project] = 0
    for _,b in dependencies:
        in_degree[b]+=1

    visited = set()
    to_visit = Queue()
    order = []

    for project in projects:
        if in_degree[project] == 0:
            to_visit.put(project)    
    while not to_visit.empty():
        current = to_visit.get()
        order.append(current)
        visited.add(current)
        neighbors = get_neighbors(current, dependencies)
        for neighbor in neighbors:
            in_degree[neighbor]-=1
            if in_degree[neighbor] == 0:
                if neighbor not in visited:
                    to_visit.put(neighbor)
                
    if len(order) < len(projects):
        return "error"
    return order

def get_neighbors(project,dependencies):
    for a,b in dependencies:
        if a == project:
            yield b

def is_valid_topological_sort(dependencies,sorted):
    index = 0
    for node in sorted:
        index+=1
        for neighbor in get_neighbors(node,dependencies):
            if neighbor in sorted[:index]:
                return False
    return True

def test_build_order():
    projects =["a", "b", "c", "d", "e", "f"]
    dependencies= [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    assert is_valid_topological_sort(dependencies,build_order(projects,dependencies)) == True
def test_when_cycle():
    projects =["a", "b", "c", "d", "e", "f"]
    dependencies= [("a", "d"),("d","b"),("b","a"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    assert build_order(projects,dependencies) == "error"
test_build_order()
test_when_cycle()

