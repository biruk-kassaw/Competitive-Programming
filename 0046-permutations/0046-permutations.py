class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(arr, visited):
            if len(arr) == len(nums):
                ans.append(list(arr))
                return 
            for num in nums:
                if num not in visited:
                    arr.append(num)
                    visited.add(num)
                    backtrack(arr, visited)
                    arr.pop()
                    visited.remove(num)
                
            
        backtrack([],set())
        return ans