class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1]*n
        print(root)
        
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            if rank[rootX] < rank[rootY]:
                root[rootX] = rootY
            elif rank[rootY] < rank[rootX]:
                root[rootY] = rootX
            else:
                root[rootX] = rootY
                rank[rootX] += 1
                
        for edge in edges:
            union(edge[0], edge[1])
            
        return find(source) == find(destination)