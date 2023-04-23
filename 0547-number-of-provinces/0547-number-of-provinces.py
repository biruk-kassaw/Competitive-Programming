class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            for neighbor in range(len(isConnected[node])):
                
                if isConnected[node][neighbor]and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        n = len(isConnected)

        visited = set()
        
        ans = 0
        
        for i in range(n):
            if i not in visited:
                ans += 1
                visited.add(i)
                dfs(i)
        
        return ans
        
        
        
        