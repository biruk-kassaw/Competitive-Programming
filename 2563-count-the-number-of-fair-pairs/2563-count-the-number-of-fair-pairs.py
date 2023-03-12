class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, cur in enumerate(nums):
            
            # low_boundary = lower - cur
            left = i + 1
            right = len(nums) - 1
            while left <= right:
                mid  = (left + right)//2
                if nums[mid] + cur < lower:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            left_boundary = left
            
            # upper_boundary = upper - cur
            left = i + 1
            right = len(nums) - 1
            
            
            # best = -1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] + cur > upper :
                    right = mid -1
                else:
                    # best = mid
                    left = mid + 1
                    
                    
            ans += right - left_boundary + 1
        return ans