class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct_position = nums[i] - 1
            if i != correct_position:
                if nums[i] == nums[correct_position]:
                    return nums[i]
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1
            
        for i in range(n):
            if num[i] != i+1:
                return nums[i]