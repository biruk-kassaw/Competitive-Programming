class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        for a, b in adjacentPairs:
            graph[a].add(b)
            graph[b].add(a)
            
        for num in graph:
            if len(graph[num]) == 1:
                first = num
                break
        ans = []
        def dfs(num):
            ans.append(num)
            for child in graph[num]:
                graph[child].remove(num)
                if child != num:
                    dfs(child)
        dfs(first)
        return ans
