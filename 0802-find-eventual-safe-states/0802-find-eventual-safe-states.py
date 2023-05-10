class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in range(len(graph)):
            adj[i].extend(graph[i])
        
        def dfs(node):
            if colors[node] == 1:
                return True
            if colors[node] == 2:
                return False
            
            colors[node] = 1
            
            for child in adj[node]:
                res = dfs(child)
                if res:
                    return True
            colors[node] = 2
            return False
        colors = [0]*len(graph)
        ans = []
        for i in range(len(graph)):
            if not dfs(i):
                ans.append(i)
        ans.sort()
        
        return ans
                
            