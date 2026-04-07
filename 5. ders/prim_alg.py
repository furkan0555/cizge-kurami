# prim algorithm
"""
minimum spanning tree algoritmasidir.
bağli, ağirlikli ve yönsüz bir grafta MST bulmak için kullamilan açgözlü bir algoritmadir.
Zaman karmaşikliği : min-heap -> O(ElogV) "E kenar V düğüm" / fibionacci-heap -> O(E + VlogV)
Biz min-heap ile yapiyoruz
"""
# u = kaynak düğüm / v = hedef düğüm / x = yeni komşular

import heapq


def prim_mst(graph, start_node):
    T = [] # MST
    S = set([start_node])# ziyaret edilenler kümesi
    Q = [] # min-heap
    
    for neighbor, weight in graph[start_node]: # hedef düğüm neighbor değişkenine, aradaki yol ise weight değişkenine atanır
        heapq.heappush(Q, (weight,start_node, neighbor)) # heapq listeyi sıralarken ilk elemana bakar, o yüzden ağırlık başta
    
    while Q:
        weight, u, v = heapq.heappop(Q) # ağırlık, kaynak düğüm, hedef düğüm 
        if v in S: # s zaten ziyaret edildiyse:
            continue # eğer ziyaret edildiyse atla
        T.append((u, v, weight)) # kenar güvenli, mst'ye ekle
        S.add(v) # ziyaret edilenlere v eklenmesinin sebebi döngü oluşmamasını sağlamak, yoksa bir düğüme 2 farklı yol oluşur
        
        for x, edge_weight in graph[v]: # ulaştığımız düğümden yeni noktalara ulaşma 
            if x not in S: 
                heapq.heappush(Q, (edge_weight, v, x)) # henüz ziyaret edilmemiş komşuları kuyruğa ekle
    return T

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


mst_sonucu = prim_mst(ornek_graf, 'A')

print("Minimum Yayilan Ağaç (MST) Kenarlari:")
toplam_maliyet = 0

for kaynak, hedef, agirlik in mst_sonucu:
    print(f"{kaynak} - {hedef} (Ağirlik: {agirlik})")
    toplam_maliyet += agirlik

print(f"\nToplam MST Maliyeti: {toplam_maliyet}")