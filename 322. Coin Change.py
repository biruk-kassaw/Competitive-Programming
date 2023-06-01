class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        @cache
        def dfs(n):
            if n == 0:
                return 0
            
            cur = float("inf")
            for coin in coins:
                if n - coin >= 0:
                    cur = min(dfs(n-coin), cur)
            return float("inf") if cur == float("inf") else cur + 1
        res = dfs(amount)
        return -1 if res == float("inf") else res
