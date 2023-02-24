class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        n = len(nums)      
        for i in range(2 * n):
            while stack and nums[i%n] > stack[-1][1]:
                next_greater[stack.pop()] = nums[i%n]
            stack.append((i%n,nums[i%n]))
            
        ans = [-1] * len(nums)
                
        for num in next_greater:
            ans[num[0]] = next_greater[num]
        return ans