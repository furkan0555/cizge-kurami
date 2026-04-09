# kruskal algorithm

"""
bağli, ağirlikli ve yönsüz bir grafta MST'yi bulmamizi sağlayan açgözlü bir algoritmadir
başlangiç düğümü yoktur
zaman karmaşikliği : O(ElogE) veya O(ElogV)
"""


def kruskal_mst(dugumler, kenarlar):
    mst = []
    parent = {}
    rank = {}
    
    for v in dugumler:
        parent[v] = v
        rank[v] = 0
        
    def find_set(item):
        if parent[item] == item:
            return item
        else:
            parent[item] = find_set(parent[item])
            return parent[item]
    
    def union(set1, set2):
        root1 = find_set(set1)
        root2 = find_set(set2)
        
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1
            
    sorted_edges = sorted(kenarlar)
    
    for weight, u, v in sorted_edges:
        if find_set(u) != find_set(v):
            mst.append((u, v, weight))
            union(u, v)
            
        
    return mst

dugumler = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# Grafın Kenarları (Edges - G.E)
# Format: (Ağırlık, Kaynak Düğüm, Hedef Düğüm)
kenarlar = [
    (4, 'A', 'B'), (8, 'A', 'H'),
    (8, 'B', 'C'), (11, 'B', 'H'),
    (7, 'C', 'D'), (2, 'C', 'I'), (4, 'C', 'F'),
    (9, 'D', 'E'), (14, 'D', 'F'),
    (10, 'E', 'F'),
    (2, 'F', 'G'),
    (1, 'G', 'H'), (6, 'G', 'I'),
    (7, 'H', 'I')
]


mst_sonucu = kruskal_mst(dugumler, kenarlar)

print("Kruskal Algoritmasi - Minimum Yayilan Ağaç (MST) Kenarlari:")
toplam_maliyet = 0

for kaynak, hedef, agirlik in mst_sonucu:
    print(f"{kaynak} - {hedef} (Ağirlik: {agirlik})")
    toplam_maliyet += agirlik

print(f"\nToplam MST Maliyeti: {toplam_maliyet}")