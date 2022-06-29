class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        begining = 0
        end = len(nums)-1
        pairs = []
        while begining < end:
            pairs.append(nums[begining] + nums[end])
            begining += 1
            end -= 1
        return max(pairs)
