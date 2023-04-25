class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        def dfs(i):
            for j in self.graph[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
                
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and (((bombs[i][0] - bombs[j][0])**2) + ((bombs[i][1] - bombs[j][1])**2))**0.5 <= bombs[i][2]:
                    self.graph[i].append(j)
        
        ans = 0
        for i in range(len(bombs)):
            visited = set([i])
            dfs(i)
            ans = max(ans, len(visited))
        return ans