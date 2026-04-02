# kruskal algorithm

"""
bağli, ağirlikli ve yönsüz bir grafta MST'yi bulmamizi sağlayan açgözlü bir algoritmadir
başlangiç düğümü yoktur
zaman karmaşikliği : O(ElogE) veya O(ElogV)
"""

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {} # her kökün ebeveynini tutacağımız sözlük yapısı
        self.rank = {} # kümelerin derinliğini tutacağımız yapı
        
        for v in vertices:
            self.parent[v] = v # başlangıçta her kümenin ebeveyni kendisidir
            self.rank[v] = 0 # başlangıçta her kümenin derinliği sıfırdır
    
    def find_set(self, item): # bu method hangi düğümün hangi köke ait olduğunu bulur
        if self.parent[item] == item: #eğer bir düğüm kendisinin ebeveyni ise; o düğüm temsici köktür
            return item 
        else: # eğer ebeveyni kendisi değilse asıl köke ulaşana kadar yukarı çıkmamız gerekir
            self.parent[item] = self.find_set(self.parent[item]) # özyinelemeli olarak asıl kökü bulur ve o an aranan düğümü en üstteki köke bağlar
            return self.parent[item] # bulunan nihai kökü döndürür
        
    def union(self, set1, set2): # iki farklı düğümün bulunduğu kümeleri birleştirir
        root1 = self.find_set(set1) 
        root2 = self.find_set(set2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal_mst(vertices, edges):
    mst_edges = []
    
    ds = DisjointSet(vertices)
    
    sorted_edges = sorted(edges)
    
    for weight, u, v in sorted_edges:
        if ds.find_set(u) != ds.find_set(v):
            mst_edges.append((u, v, weight))
            ds.union(u, v)
    
    return mst_edges

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