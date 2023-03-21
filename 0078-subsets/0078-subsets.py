class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        
        def backtrack(arr, idx):
            for i in range (idx,len(nums)):
                arr.append(nums[i])
                ans.append(list(arr))
                backtrack(arr, i+1)
                arr.pop()
        backtrack([],0)
        return ans
                
                