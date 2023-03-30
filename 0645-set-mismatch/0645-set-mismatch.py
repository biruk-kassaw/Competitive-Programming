class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        while i < n:
            correct_position = nums[i] - 1
            if nums[i] != nums[correct_position]:
                nums[correct_position], nums[i] = nums[i], nums[correct_position]
            else:
                i += 1
        res = []
        for i in range(n):
            if i+1 != nums[i]:
                res.append(nums[i])
                res.append(i+1)
                
        return res