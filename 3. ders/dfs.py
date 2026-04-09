#dfs algorithm

from collections import deque


def dfs(graph, start):
    visited = {start}
    stack = deque([start])
    
    while stack:
        vertex = stack.pop()
        print(vertex,end=(' '))
        
        for n in graph[vertex]:
            if n not in visited:
                stack.append(n)
                visited.add(n)
                
                
graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A'],
    'C' : ['A', 'E','F'],
    'D' : ['A'],
    'E' : ['C'],
    'F' : ['C', 'G'],
    'G' : ['F']
}

dfs(graph,'A')