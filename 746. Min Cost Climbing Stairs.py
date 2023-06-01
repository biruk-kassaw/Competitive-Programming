class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(n):
            if n < 0:
                return 0
            
            if n == 0:
                return cost[0]
            
            two = dfs(n - 2) + cost[n]
            one = dfs(n-1) + cost[n]
            return min(two, one)
        
        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))
