class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        n = len(nums)   
        ans = [-1] * len(nums)
        
        for i in range(2 * n):
            while stack and nums[i%n] > stack[-1][1]:
                ans[stack.pop()[0]] = nums[i%n]
            stack.append((i%n,nums[i%n]))
            
        return ans
    
    
    
    
    
    