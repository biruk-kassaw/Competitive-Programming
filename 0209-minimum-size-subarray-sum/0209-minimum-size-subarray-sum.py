class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        summ = 0
        min_length = float("inf")
        for i in range(len(nums)):
            summ += nums[i]
            while summ-nums[left] >= target:
                summ -= nums[left]
                left += 1
            if summ >= target:
                min_length = min(min_length, i-left + 1)
        return min_length if min_length != float("inf") else 0