class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            correct_position = nums[i]
            if nums[i] < n and i != correct_position:
                nums[correct_position], nums[i] = nums[i], nums[correct_position]
            else:
                i += 1
        for i in range(n):
            if i != nums[i]:
                return i
        return len(nums)