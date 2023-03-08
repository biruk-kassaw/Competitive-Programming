class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        seen = {0:1}
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - goal in seen:
                ans += seen[running_sum - goal]
            seen[running_sum] = seen.get(running_sum,0) + 1
        return ans
    