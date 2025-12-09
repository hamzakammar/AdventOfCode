with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    coords = [[int(x) for x in line.split(',') ] for line in lines]

def dist(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(len(a)))

n = len(coords)

dists = []
for i in range(n):
    for j in range(i + 1, n): 
        dists.append((dist(coords[i], coords[j]), i, j))
dists.sort()

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n 

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_x = self.find(u)
        root_y = self.find(v)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.count -= 1
            return True
        return False

CHECK = 1000
uf = UnionFind(n)

for idx in range(min(CHECK, len(dists))):
    _, u, v = dists[idx]
    uf.union(u, v)

cluster_sizes = {}
for i in range(n):
    root = uf.find(i)
    cluster_sizes[root] = cluster_sizes.get(root, 0) + 1

sizes = sorted(cluster_sizes.values(), reverse=True)
print(sizes[0] * sizes[1] * sizes[2])

uf2 = UnionFind(n)

for d, i, j in dists:
    uf2.union(i, j)
    
    # Check if all connected (all have same root)
    if uf2.count == 1:
        print(coords[i][0] * coords[j][0])
        break