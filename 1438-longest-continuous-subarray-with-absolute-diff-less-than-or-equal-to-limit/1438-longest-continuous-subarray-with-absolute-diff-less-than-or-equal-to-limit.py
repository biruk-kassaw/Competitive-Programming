class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_stack = deque()
        max_stack = deque()
        length = 0
        left = 0
        for i in range(len(nums)):
            while min_stack and nums[i] < min_stack[-1]:
                min_stack.pop()
                
            while max_stack and nums[i] > max_stack[-1]:
                max_stack.pop()
                
            min_stack.append(nums[i])
            max_stack.append(nums[i])
            
            while max_stack and min_stack and abs(max_stack[0] - min_stack[0]) > limit:
                if nums[left] == min_stack[0]:
                    min_stack.popleft()
                if nums[left] == max_stack[0]:
                    max_stack.popleft()
                left += 1
                    
            length = max(length, i-left + 1)
        return length
            
        