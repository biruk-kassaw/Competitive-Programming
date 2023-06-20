class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cur, free = [0] * n, [0] * n
        cur[0] = -prices[0]
        
        for i in range(1, n):
            cur[i] = max(cur[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], cur[i - 1] + prices[i] - fee)
        
        return free[-1]
