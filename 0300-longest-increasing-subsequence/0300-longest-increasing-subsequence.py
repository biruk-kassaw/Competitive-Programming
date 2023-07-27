class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        for i in range(n-1,-1,-1):
            local = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    local = max(local, 1+dp[j])
            dp[i] = local
        return max(dp.values())