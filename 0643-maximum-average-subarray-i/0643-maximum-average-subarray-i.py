class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start_i = 0
        end_i = 0
        max_sum = float("-inf")
        cur_sum = 0
        while end_i < len(nums):
            cur_sum += nums[end_i]
            if end_i >= k-1:
                max_sum = max(max_sum, cur_sum/k)
                cur_sum -= nums[start_i]
                start_i += 1
            end_i += 1
        return max_sum