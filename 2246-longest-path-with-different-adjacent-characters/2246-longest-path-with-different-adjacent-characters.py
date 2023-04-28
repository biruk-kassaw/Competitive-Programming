class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for i in range(1, len(parent)):
            graph[(s[parent[i]], parent[i])].append((s[i], i))
            
        self.max_len = 1
        def dfs(root):
            if root not in graph:
                return 1
            
            max_child_count = 0
            second_max_child = 0
            
            for child in graph[root]:
                res = dfs(child)
                if root[0] != child[0]:
                    if max_child_count< res:
                        max_child_count,second_max_child = res, max_child_count
                    elif second_max_child<res:
                        second_max_child = res
                        
            total_child_count = max_child_count + second_max_child +1
            self.max_len = max(self.max_len,total_child_count)
        
            
            return max_child_count + 1
            
          
        dfs((s[0], 0))
        return self.max_len
