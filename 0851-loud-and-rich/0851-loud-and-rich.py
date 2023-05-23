class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        visited = {}
        def dfs(node, minVal):
            if node in visited:
                return visited[node]
        
            for child in graph[node]:
                if child in visited:
                    minVal = min (minVal, visited[child])
                else:
                    curMin = dfs(child, quiet[child])
                    visited[child] = curMin
                    minVal = min(minVal, curMin)
                    
            return minVal
        
        ans = []
        dic = {}
        
        for i in range(len(quiet)):
            dic[quiet[i]] = i
        
        for i in range(len(quiet)):
            ans.append(dic[dfs(i, quiet[i])])
            
        return ans