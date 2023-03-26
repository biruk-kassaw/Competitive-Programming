class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backtrack(nums,res):
            if len(res)>1:
                ans.add(res)
            if not nums:
                return
            
            for i in range(len(nums)):

                if not res or res[-1]<=nums[i]:
                    backtrack(nums[i+1:],res+(nums[i],))
        backtrack(nums,())
        return ans