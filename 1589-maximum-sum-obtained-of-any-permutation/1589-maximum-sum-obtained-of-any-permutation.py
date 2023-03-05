class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        for request in requests:
            prefix[request[0]] += 1
            prefix[request[1] + 1] -= 1
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        nums.sort()
        prefix.sort()
        
        ans = 0
        i = len(prefix) - 1
        j = len(nums) - 1 
        
        while prefix[i] != 0 and i > -1:
            ans += prefix[i]*nums[j]
            i -= 1
            j -= 1
        return ans % (10**9 + 7)