class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, target, maxLen, curSum = 0, sum(nums) - x, -1, 0
        if target < 0:
            return -1
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum > target:
                curSum -= nums[l]
                l += 1 
            if curSum == target:
                maxLen = max(maxLen, r - l + 1)
                
        return len(nums) - maxLen if maxLen != -1 else -1