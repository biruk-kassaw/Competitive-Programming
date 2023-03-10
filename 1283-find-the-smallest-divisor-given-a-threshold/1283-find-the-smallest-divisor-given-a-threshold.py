class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = -1
        while left <= right:
            mid = (left + right)//2
            _sum = 0
            for num in nums:
                _sum += math.ceil(num/mid)
            if _sum > threshold:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans
    