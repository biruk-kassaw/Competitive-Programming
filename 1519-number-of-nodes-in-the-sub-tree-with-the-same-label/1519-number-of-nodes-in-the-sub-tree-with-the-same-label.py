class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
                
        def dfs(node, prev):
            total_dict = Counter()
            total_dict[labels[node]] = 1
            for child in graph[node]:
                if child == prev:
                    continue
                total_dict += dfs(child, node)
                
            ans[node] = total_dict[labels[node]]
            return total_dict
    
        dfs(0, None)
        return ans