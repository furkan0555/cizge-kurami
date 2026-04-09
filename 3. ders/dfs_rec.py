def dfs_rec(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start,end=(' '))
    
    for v in graph[start]:
        if v not in visited:
            dfs_rec(graph, v, visited)
        
graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A'],
    'C' : ['A', 'E','F'],
    'D' : ['A'],
    'E' : ['C'],
    'F' : ['C', 'G'],
    'G' : ['F']
}


dfs_rec(graph, 'A')