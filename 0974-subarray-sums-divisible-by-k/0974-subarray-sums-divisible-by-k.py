class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sums = {0:1}
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum % k in  prefix_sums:
                ans += prefix_sums[running_sum%k]
            prefix_sums[running_sum%k] = prefix_sums.get(running_sum%k,0) + 1
            
        return ans