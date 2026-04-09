from collections import deque
"""
BFS Breadth First Search algorithm
kuyruk veri yapisi kullanilir
unweighted graflarda gerekli olur
Zaman karmasikligi O(V + E)
V = vertex (düğüm)
E = edges (kenar)
Alan karmasikligi O(V)
"""

graph = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A'],
    'C' : ['A', 'E','F'],
    'D' : ['A'],
    'E' : ['C'],
    'F' : ['C', 'G'],
    'G' : ['F']
}

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    vertex_ops = 0
    edge_ops = 0
    while queue:
        vertex = queue.popleft()
        vertex_ops += 1
        print(vertex,end=(' '))
        for n in graph[vertex]:
            edge_ops += 1
            if n not in visited:
                queue.append(n)
                visited.add(n)
    print(f"\nToplam işlem: {vertex_ops + edge_ops}")
    
bfs(graph,'A')
