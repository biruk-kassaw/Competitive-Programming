class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)   
        ans = [-1] * len(nums)
        
        for i in range(2 * n):
            while stack and nums[i%n] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i%n]
            stack.append(i%n)
            
        return ans
    
    
    
    
    
    