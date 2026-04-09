from collections import deque


def BFS_shortest_path(graph, start, goal):
    visited = {start}
    kuyruk = deque([start])
    parent = {}
    parent[start] = None
    path = []
    
    while kuyruk:
        vertex = kuyruk.popleft()
        print(vertex, end=(' '))
        
        if vertex == goal:
            break
        
        for v in graph[vertex]:
            if v not in visited:
                visited.add(v)
                kuyruk.append(v)
                parent[v] = vertex

    
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A'],
    'C' : ['A', 'E','F'],
    'D' : ['A'],
    'E' : ['C'],
    'F' : ['C', 'G'],
    'G' : ['F']
}

path = BFS_shortest_path(graph, 'A', 'G')
print()
print(path)