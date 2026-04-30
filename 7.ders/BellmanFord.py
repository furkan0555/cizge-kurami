D = {} # distance
P = {} # source


def bellmanford(E, V, start):
    for a in V:
        D[a] = float('inf')
        P[a] = None
    D[start] = 0
    
    
    k = 0
    while (k < len(V)):
        k += 1
        for u, v, edge_weight in E:
            if D[v] > D[u] + edge_weight:
                D[v] = D[u] + edge_weight
                P[v] = u
        
    return D, P
    
        
    

V = ["A", "B", "C", "D", "E", "F", "G"]
E = [
    ("A", "B", 2),
    ("A", "D", 5),
    ("A", "F", 3),
    ("B", "E", 1),
    ("C", "B", 7),
    ("C", "G", 4),
    ("D", "E", 1),
    ("E", "C", -3),
    ("E", "G", 3),
    ("F", "B", -4),
    ("G", "D", -1)
]
start = "A"

dist, source = bellmanford(E, V, start)
print(dist)
print(source)