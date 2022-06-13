class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bins = [0 for _ in range(3)]
        for col in nums:
            bins[col] += 1
        for i in range(len(nums)):
            if bins[0]:
                nums[i] = 0
                bins[0] -= 1
            elif bins[1]:
                nums[i] = 1
                bins[1] -= 1
            else:
                nums[i] = 2
