class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        l,r = 0,len(nums)-1
        while len(ans) != len(nums):
            ans.append(nums[l])
            l += 1
            if l <= r:
                ans.append(nums[r])
                r -= 1
        return ans
