#dijktra algorithm

"""
ağirlikli graflarda en kisa yol problemini çözen bir algoritmadir
açgözlü bir yaklaşim benimser
kenar ağirliklari negatif olmamalidir
zaman karmaşikliği: dizi ile = O(v^2) / priority queue ile = O(ElogV)
seyrek graflar için çok daha verimlidir
"""


import heapq

def dijktra(graph, start):
    D = {} # uzaklık
    P = {} # source
    Q = [] # priority queue
    
    for v in graph: 
        D[v] = float('inf') # bütün düğümlerin uzaklığı sonsuz yapılır
            
    D[start] = 0 # başlangıç düğümün uzaklığı sıfır yapılır
        
    
    heapq.heappush(Q, (0, start))
    
    while Q:
        cur_dist, u = heapq.heappop(Q)
        
        if cur_dist > D[u]: # kuyruk tekrar tekrar çalışmasın diye konulan satır, kod bu olmadan yavaş çalışır
            continue
        
        
        for v, edge_weight in graph[u]: 
            if D[v] > D[u] + edge_weight:
                D[v] = D[u] + edge_weight
                P[v] = u
                heapq.heappush(Q, (D[v], v)) # güncellenmiş düğüm tekrar kuyruğa atılır
    
    return D, P

ornek_graf = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('C', 8), ('H', 11)],
    'C': [('B', 8), ('D', 7), ('I', 2), ('F', 4)],
    'D': [('C', 7), ('E', 9), ('F', 14)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('H', 1), ('I', 6)],
    'H': [('A', 8), ('B', 11), ('G', 1), ('I', 7)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}




mesafeler, rotalar = dijktra(ornek_graf,'A')

print("A düğümünden diğer düğümlere en kisa mesafeler:")
print(mesafeler)
print("hangi düğüme nereden geldik")
print(rotalar)