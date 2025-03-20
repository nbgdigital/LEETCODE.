from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weight = [(1 << 17) - 1] * n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int, w: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            self.weight[rootX] &= w
            return
        
        newWeight = self.weight[rootX] & self.weight[rootY] & w
        self.weight[rootX] = newWeight
        self.weight[rootY] = newWeight
        
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
    
    def getMinCost(self, u: int, v: int) -> int:
        if u == v:
            return 0
        rootU = self.find(u)
        rootV = self.find(v)
        return self.weight[rootU] if rootU == rootV else -1


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)
        return [uf.getMinCost(s, t) for s, t in query]
