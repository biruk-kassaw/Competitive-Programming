class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixsum = [0]
        for i in range(len(nums)):
            self.prefixsum.append(self.nums[i] + self.prefixsum[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right + 1] - self.prefixsum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)