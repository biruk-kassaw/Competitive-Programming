class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
            
        def dfs(node):
            if not ans[node]:
                ans[node] = node
                for child in graph[node]:
                    cur = dfs(child)
                    if quiet[cur] < quiet[ans[node]]:
                        ans[node] = cur
            return ans[node]
        
        ans = [None] * len(quiet)
        
        for i in range(len(quiet)):
            dfs(i)
            
        return ans