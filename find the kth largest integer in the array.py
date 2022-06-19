class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=self.sorter)
        return(nums[len(nums)-k])
    def sorter(self,nums):
        return int(nums)
